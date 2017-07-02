#!/usr/bin/python
# coding=utf-8

import data_save_to_redis as cache


def cal(log={}, keys=[]):
    if isinstance(keys, type([])):
        skey = "sim="
        for key in keys:
            if key in log.keys():
                skey = skey + "|" + log[key]
        cache.addOne(skey)
