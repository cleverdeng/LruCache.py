#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""

import lru as cache

lru = cache.LruCache(item_max=5)

@lru.fn_cache
def test_fn(x,y):
    return x,y

print test_fn(1,2)
print test_fn(1,2)
print test_fn(3,4)
print 'get key:test value:%s' % lru.get("test1") 
lru.put('test1', 1)
lru.put("test2", 2)
lru.put("test3", 3)
lru.put("test4", 4)
lru.put("test5", 5)
print 'get key:test value:%s' % lru.get("test1") 
lru.put("test6", 6)
lru.put("test7", 7) 
print 'get key:test6 value:%s' % lru.get("test6") 
print 'get key:test3 value:%s' % lru.get("test3") 
lru.status()   
