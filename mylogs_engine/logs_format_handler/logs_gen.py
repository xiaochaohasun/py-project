#!/usr/bin/env python

from urllib import urlopen

for i in range(10):
    url ="http://127.0.0.1/py/%s" % i
    urlopen(url)
    print url
