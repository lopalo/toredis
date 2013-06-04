import zlib

from bisect import bisect
from functools import partial
from tornado.gen import coroutine

from toredis.client import ClientPool as BasicClientPool
from toredis.commands_future import RedisCommandsFutureMixin


class ClientPool(RedisCommandsFutureMixin, BasicClientPool):
    pass


class RedisNodes(object):
    pool_cls = ClientPool # should be subclass of ClientPool

    def __init__(self, *, nodes, default_max_clients=100,
                                 default_replicas=100):
        self._hash_to_nodeinfo = {}
        self._hash_to_client = {}
        self.nodes = []
        for n in nodes:
            cli = self.pool_cls(host=n.get('host'),
                                port=n.get('port'),
                                unix_socket=n.get('unix_socket'),
                                max_clients=n.get('max_clients',
                                                default_max_clients),
                                db=n['db'],
                                password=n.get('password'))

            self.nodes.append((n, cli))
            for num in range(n.get('replicas', default_replicas)):
                _hash = self.hash_func('{}: {}'.format(n['name'], num))
                self._hash_to_nodeinfo[_hash] = n
                self._hash_to_client[_hash] = cli

        self._hash_list = sorted(self._hash_to_client)

    def hash_func(self, string):
        return zlib.crc32(string.encode('utf-8'))

    def _get_node_hash(self, key):
        _hash = self.hash_func(key)
        idx = bisect(self._hash_list, _hash)
        if idx == len(self._hash_list):
            idx = 0
        return self._hash_list[idx]

    def get_client(self, key):
        _node_hash = self._get_node_hash(key)
        return self._hash_to_client[_node_hash]

    def get_info(self, key):
        _node_hash = self._get_node_hash(key)
        return self._hash_to_nodeinfo[_node_hash]

    def __getitem__(self, key):
        return self.get_client(key)

    @coroutine
    def check_nodes(self):
        """ Checks connections with all nodes and setups db_name """

        for info, cli in self.nodes:
            yield cli.setnx('db_name', info['name'])
