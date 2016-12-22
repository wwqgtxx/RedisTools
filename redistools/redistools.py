#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# author wwqgtxx <wwqgtxx@gmail.com>
from __future__ import (absolute_import, division,
                        print_function, unicode_literals)
from future import standard_library

standard_library.install_aliases()
from builtins import *
import uuid

import redis_collections
import redis_lock


class RedisDict(redis_collections.Dict):
    CLASS_PREFIX = "RedisDict:AutoUUID:"

    def _create_key(self):
        return RedisDict.CLASS_PREFIX + (super(RedisDict, self)._create_key())


class RedisList(redis_collections.List):
    CLASS_PREFIX = "RedisList:AutoUUID:"

    def _create_key(self):
        return RedisList.CLASS_PREFIX + (super(RedisList, self)._create_key())


class RedisLock(redis_lock.Lock):
    CLASS_PREFIX = "RedisLock:AutoUUID:"

    def _create_key(self):
        return RedisList.CLASS_PREFIX + uuid.uuid4().hex

    def __init__(self, redis, key=None, expire=None, auto_renewal=False):
        """
        :param redis:
            An instance of :class:`~StrictRedis`.
        :param key:
            The name (redis key) the lock should have.
        :param expire:
            The lock expiry time in seconds. If left at the default (None)
            the lock will not expire.
        :param auto_renewal:
            If set to ``True``, Lock will automatically renew the lock so that it
            doesn't expire for as long as the lock is held (acquire() called
            or running in a context manager).

            Implementation note: Renewal will happen using a daemon thread with
            an interval of ``expire*2/3``. If wishing to use a different renewal
            time, subclass Lock, call ``super().__init__()`` then set
            ``self._lock_renewal_interval`` to your desired interval.
        """
        if not key:
            key = self._create_key()
        self.key = key
        super(RedisLock, self).__init__(redis_client=redis, name=key, expire=expire,
                                        auto_renewal=auto_renewal)
