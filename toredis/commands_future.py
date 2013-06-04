from toredis.commands import RedisCommandsMixin
from tornado.concurrent import return_future


class RedisCommandsFutureMixin(RedisCommandsMixin):

    for mname in dir(RedisCommandsMixin):
        meth = getattr(RedisCommandsMixin, mname)
        if mname.startswith('_') or not callable(meth):
            continue
        locals()[mname] = return_future(meth)
