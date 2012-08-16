#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    Author:cleverdeng
    E-mail:clverdeng@gmail.com
"""
from distutils.core import setup
from lru import __version__ as version

setup(
            name='lru',
            version=version,
            description='Implements LRU(least recently used) cache algorithm, Support the thread safe, With Python',
            author='cleverdeng',
            author_email='cleverdeng@gmail.com',
            url='http://github.com/cleverdeng/LruCache.py',
            py_modules=['lru'],
            license='MIT License',
            platforms=['any'],
            classifiers=[
                'Development Status :: 4 - Beta',
                'Intended Audience :: Developers',
                'License :: OSI Approved :: MIT License',
                'Programming Language :: Python',
                'Topic :: Software Development',
                'Topic :: Software Development :: Libraries',
                'Topic :: Software Development :: Libraries :: Python Modules'
                ]
                    
    )
