LruCache.py
======

Implements LRU(Last-recently-used) cache algorithm, Support the thread safe, With Python


Example:

<code>
import lru as cache

<code>
lru = cache.LruCache(item_max=5)
      
<code>
@lru.fn_cache
<code>
def test_fn(x,y):
<code>
    return x,y

</code>
