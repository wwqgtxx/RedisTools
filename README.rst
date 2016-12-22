RedisTools
=================
A Redis tools provide python's Lock RLock Semaphore BoundedSemaphore Condition Event Barrier and Queue cross process

Quickstart
----------
Install the library with ``pip install redistools``.
Import the collections from the top-level ``redistools`` package.

.. code-block:: python
    from redismanager import RedisManager as Manager
    manager = Manager()

Then use it as a standard multiprocessing.Manager <https://docs.python.org/3/library/multiprocessing.html#multiprocessing.managers.SyncManager>

Notice: We didn't provide ``Array`` and ``Value`` in ``RedisManager``

© 2016-? wwqgtxx
