#!/usr/bin/env python

import  redis
import logs_reader

r=redis.Redis(host='127.0.0.1',port=6379)

for line in file('/data/user/nginx_log/py_format.log'):
    if line.find('play')>0:

        count=r.get('play_count')
        if not count:count =0
        count=int(count)+1

        r.set('play_count',count)
