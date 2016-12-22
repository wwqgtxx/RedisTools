#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author wwqgtxx <wwqgtxx@gmail.com>
# a simply lib base on redistools to replace python's multiprocessing.Manager
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future import standard_library

standard_library.install_aliases()
from builtins import *

from .redistools import *
from redis import StrictRedis
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

    def dict(self, data=None):
        result = RedisDict(data=data, redis=self._redis)
        logger.info("create new RedisDict with key<%s>" % str(result.key))
        return result

    def list(self, data=None):
        result = RedisList(data=data, redis=self._redis)
        logger.info("create new RedisList with key<%s>" % str(result.key))
        return result

    def Lock(self):
        result = RedisLock(redis=self._redis)
        logger.info("create new RedisLock with key<%s>" % str(result.key))
        return result

    def RLock(self):
        result = RedisRLock(redis=self._redis)
        logger.info("create new RedisRLock with key<%s>" % str(result.key))
        return result

    def Semaphore(self, value=1):
        result = RedisSemaphore(value=value, redis=self._redis)
        logger.info("create new RedisSemaphore with key<%s>" % str(result.key))
        return result

    def BoundedSemaphore(self, value=1):
        result = RedisBoundedSemaphore(value=value, redis=self._redis)
        logger.info("create new RedisBoundedSemaphore with key<%s>" % str(result.key))
        return result

    def Condition(self, lock=None):
        result = RedisCondition(lock=lock, redis=self._redis)
        logger.info("create new RedisCondition with key<%s>" % str(result.key))
        return result

    def Event(self):
        result = RedisEvent(redis=self._redis)
        logger.info("create new RedisEvent with key<%s>" % str(result.key))
        return result

    def Barrier(self, parties, action=None, timeout=None):
        result = RedisBarrier(parties=parties, action=action, timeout=timeout, redis=self._redis)
        logger.info("create new RedisBarrier with key<%s>" % str(result.key))
        return result

    def Queue(self, maxsize=0):
        result = RedisQueue(maxsize=maxsize, redis=self._redis)
        logger.info("create new RedisQueue with key<%s>" % str(result.key))
        return result
