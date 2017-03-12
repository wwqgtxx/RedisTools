#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author wwqgtxx <wwqgtxx@gmail.com>
# a simply lib base on redistools to replace python's multiprocessing.Manager
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)

from .redistools import *
from redis import StrictRedis
import time
import logging

logger = logging.getLogger(__name__)


class RedisManager(object):
    def __init__(self, host='localhost', port=6379, db=0, redis=None, **kwargs):
        self.host = host
        self.port = port
        self.db = db
        if redis:
            self._redis = redis
            try:
                redis_kwargs = self._redis.connection_pool.connection_kwargs
                self.host = redis_kwargs.get('host')
                self.port = redis_kwargs.get('port')
                self.db = redis_kwargs.get('db')
            except:
                pass
        else:
            self._redis = StrictRedis(host=host, port=port, db=db, **kwargs)
        for i in range(3):
            if not self._redis.ping():
                time.sleep(1)
            else:
                break
        else:
            logger.warning("redis can't connect!")

    def dict(self, data=None, key=None, log=logger):
        result = RedisDict(data=data, redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisDict with key<%s>" % str(result.key))
            else:
                log.info("get RedisDict with key<%s>" % key)
        return result

    def list(self, data=None, key=None, log=logger):
        result = RedisList(data=data, redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisList with key<%s>" % str(result.key))
            else:
                log.info("get RedisList with key<%s>" % key)
        return result

    def Namespace(self, key=None, log=logger):
        result = RedisNamespace(redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisNamespace with key<%s>" % str(result.key))
            else:
                log.info("get RedisNamespace with key<%s>" % key)
        return result

    def Lock(self, key=None, log=logger):
        result = RedisLock(redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisLock with key<%s>" % str(result.key))
            else:
                log.info("get RedisLock with key<%s>" % key)
        return result

    def RLock(self, key=None, log=logger):
        result = RedisRLock(redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisRLock with key<%s>" % str(result.key))
            else:
                log.info("get RedisRLock with key<%s>" % key)
        return result

    def Semaphore(self, value=1, key=None, log=logger):
        result = RedisSemaphore(value=value, redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisSemaphore with key<%s>" % str(result.key))
            else:
                log.info("get RedisSemaphore with key<%s>" % key)
        return result

    def BoundedSemaphore(self, value=1, key=None, log=logger):
        result = RedisBoundedSemaphore(value=value, redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisBoundedSemaphore with key<%s>" % str(result.key))
            else:
                log.info("get RedisBoundedSemaphore with key<%s>" % key)
        return result

    def Condition(self, lock=None, key=None, log=logger):
        result = RedisCondition(lock=lock, redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisCondition with key<%s>" % str(result.key))
            else:
                log.info("get RedisCondition with key<%s>" % key)
        return result

    def Event(self, key=None, log=logger):
        result = RedisEvent(redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisEvent with key<%s>" % str(result.key))
            else:
                log.info("get RedisEvent with key<%s>" % key)
        return result

    def Barrier(self, parties, action=None, timeout=None, key=None, log=logger):
        result = RedisBarrier(parties=parties, action=action, timeout=timeout, redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisBarrier with key<%s>" % str(result.key))
            else:
                log.info("get RedisBarrier with key<%s>" % key)
        return result

    def Queue(self, maxsize=0, key=None, log=logger):
        result = RedisQueue(maxsize=maxsize, redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisQueue with key<%s>" % str(result.key))
            else:
                log.info("get RedisQueue with key<%s>" % key)
        return result

    def Pipe(self, maxsize=0, key=None, log=logger):
        result = RedisPipe(maxsize=maxsize, redis=self._redis, key=key)
        if log:
            if not key:
                log.info("create new RedisPipe with key<%s>" % str(result.key))
            else:
                log.info("get RedisPipe with key<%s>" % key)
        return result
