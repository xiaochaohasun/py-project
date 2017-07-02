#!/usr/bin/python
# coding=utf-8
"""
python 操作redis是很方便的,直接安装此包
注意:在docker中重启redis,导致数据完全丢失

"""

import redis

r = redis.Redis(host='127.0.0.1', port=6379)


def addOne(key):
    add(key, 1)


def add(key, num):
    val = r.get(key)
    if val == None:
        val = 0
    else:
        val = int(r.get(key))
    r.set(key, str(val + num))


def getkeys(pattern=""):
    return r.keys(pattern)


def get(key=""):
    return r.get(key)


def addSet(key="", uid=""):
    r.sadd(key, uid)


def getSet(key=""):
    return r.scard(key)

