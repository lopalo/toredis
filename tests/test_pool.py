from tornado.testing import AsyncTestCase
from toredis.client import ClientPool

class TestPool(AsyncTestCase):

    def test_get_new_client(self):
        pool = ClientPool(max_clients=5)
        cli1 = pool.get_client()
        cli1.send_message(['PING'])
        cli2 = pool.get_client()
        self.assertIsNot(cli1, cli2)

    def test_get_existing_client(self):
        pool = ClientPool(max_clients=5)
        cli1 = pool.get_client()
        cli1.callbacks = []
        cli2 = pool.get_client()
        self.assertIs(cli1, cli2)

    def test_limit(self):
        pool = ClientPool(max_clients=2)
        cli1 = pool.get_client()
        cli1.send_message(['PING'])
        cli2 = pool.get_client()
        cli2.send_message(['PING'])
        cli3 = pool.get_client()
        self.assertIn(cli3, [cli1, cli2])


