LruCache.py
======

Implements LRU(Last-recently-used) cache algorithm, Support the thread safe, With Python


Example:

<code>
import lru as cache

lru = cache.LruCache(item_max=5)
      
@lru.fn_cache
def test_fn(x,y):
    return x,y

</code>
