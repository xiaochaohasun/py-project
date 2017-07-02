#!/usr/bin/env python
# -*- coding:utf-8 -*-

'''
时间/IP/Device/MAC/USER/APP/VER/ACT/Object
'''

import random
import time
import datetime
import sys
sys.path.append("..")
from defines import *



ips = {'120.25.63.167': ('深圳市', '广东省'),
       '58.21.1.2': ('佛山市', '广东省'),
       '58.207.96.2': ('南京市', '江苏省'),
       '218.4.58.31': ('苏州市', '江苏省'),
       '59.76.192.3': ('银川市', '宁夏回族自治区'),
       '222.75.147.198': ('吴忠市', '宁夏回族自治区')
       }

dates=["2016/5/10","2016/5/11","2016/5/12",
       "2016/5/13","2016/5/14","2016/5/15",
       "2016/5/16"
       ]

def getTime():
    dateindex = random.randint(0, len(dates) - 1)
    hours = random.randint(0, 23)
    mins = random.randint(0, 59)
    seconds = random.randint(0, 59)
    stime = dates[dateindex] + ":" + str(hours) + ":" + str(mins) + ":" + str(seconds)

    dtime = datetime.datetime.strptime(stime, "%Y/%m/%d:%H:%M:%S")
    dtime = time.mktime(dtime.timetuple())
    dtime = int(dtime)
    return dtime

def getIP():
    index = random.randint(0, len(ips) - 1)
    ip = ips.keys()[index]
    return ip

def format_log(orilog=''):
    s=orilog.split('[')
    ss=s[4].replace(']','').split('/')
    print orilog,ss
    logs={
    "dtime":getTime(),
    "ip":getIP(),
    "device":ss[4],
    "mac":ss[3],
    "user":ss[2],
    "app":ss[5],
    "ver":ss[6],
    "act":ss[7],
    "obj":ss[8],
    }
    res = "%s/%s/%s/%s/%s/%s/%s/%s/%s" % (
        logs['dtime'], logs['ip'], logs['device'],
        logs['mac'], logs['user'], logs['app'],
        logs['ver'], logs['act'], logs['obj'])
    print res
    return res

if __name__ == '__main__':

    f = file("../data/standard/std_user_behavior.log", "w")

    for line in file("../data/original/user_behavior.log", "r"):
        f.write(format_log(line) + "\n")

    f.close()



