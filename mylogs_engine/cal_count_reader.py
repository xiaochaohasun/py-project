#!/usr/bin/env python

import  redis
import logs_reader as logreader

r=redis.Redis(host='127.0.0.1',port=6379)


def cal(par=['device','act']):
    reader=logreader.Reader('/data/user/nginx_log/py_format.log')

    while True:
        log = reader.read()
        if not log:
            break
        print log

        key=''
        for i in par:
            key+='_'+log[i]

        print key

        count=r.get(key)
        if not count:
            count= 0
        count=int(count)+1

        r.set(key,count)

cal(['user','device'])