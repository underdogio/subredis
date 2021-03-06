from functools import partial
from types import MethodType


def sampleSpy(spyObj, methodName, *args, **kwargs):
    spyObj.lastCall = methodName
    spyObj.lastArgs = args
    spyObj.lastKwargs = kwargs


class RedisSpy(object):
    """ Report on how "redis" is being called
        in testing"""
    def __init__(self):
        self.addSpy("append")
        self.addSpy("bitcount")
        self.addSpy("blpop")
        self.addSpy("brpop")
        self.addSpy("debug_object")
        self.addSpy("decr")
        self.addSpy("delete")
        self.addSpy("exists")
        self.addSpy("expire")
        self.addSpy("expireat")
        self.addSpy("get")
        self.addSpy("getbit")
        self.addSpy("getrange")
        self.addSpy("getset")
        self.addSpy("hdel")
        self.addSpy("hexists")
        self.addSpy("hget")
        self.addSpy("hgetall")
        self.addSpy("hincrby")
        self.addSpy("hincrbyfloat")
        self.addSpy("hkeys")
        self.addSpy("hlen")
        self.addSpy("hmget")
        self.addSpy("hmset")
        self.addSpy("hset")
        self.addSpy("hsetnx")
        self.addSpy("hvals")
        self.addSpy("incr")
        self.addSpy("incrbyfloat")
        self.addSpy("lindex")
        self.addSpy("linsert")
        self.addSpy("llen")
        self.addSpy("lock")
        self.addSpy("lpop")
        self.addSpy("lpush")
        self.addSpy("lpushx")
        self.addSpy("lrange")
        self.addSpy("lrem")
        self.addSpy("lset")
        self.addSpy("ltrim")
        self.addSpy("mget")
        self.addSpy("persist")
        self.addSpy("pexpire")
        self.addSpy("pexpireat")
        self.addSpy("ping")
        self.addSpy("pipeline")
        self.addSpy("pttl")
        self.addSpy("rpop")
        self.addSpy("rpush")
        self.addSpy("rpushx")
        self.addSpy("sadd")
        self.addSpy("scard")
        self.addSpy("set")
        self.addSpy("setbit")
        self.addSpy("setex")
        self.addSpy("setnx")
        self.addSpy("setrange")
        self.addSpy("sinter")
        self.addSpy("sismember")
        self.addSpy("smembers")
        self.addSpy("spop")
        self.addSpy("srandmember")
        self.addSpy("srem")
        self.addSpy("substr")
        self.addSpy("sunion")
        self.addSpy("time")
        self.addSpy("ttl")
        self.addSpy("type")
        self.addSpy("zadd")
        self.addSpy("zcard")
        self.addSpy("zincrby")
        self.addSpy("zinterstore")
        self.addSpy("zrange")
        self.addSpy("zrangebyscore")
        self.addSpy("zrank")
        self.addSpy("zrem")
        self.addSpy("zremrangebyrank")
        self.addSpy("zremrangebyscore")
        self.addSpy("zrevrange")
        self.addSpy("zrevrangebyscore")
        self.addSpy("zrevrank")
        self.addSpy("zscore")

    def addSpy(self, methodName):
        spyMethod = MethodType(sampleSpy, self)
        spyBoundToName = partial(spyMethod, methodName)
        spyBoundToName.__name__ = methodName
        setattr(self, methodName, spyBoundToName)
