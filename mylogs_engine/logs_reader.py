#!/usr/bin/python
# coding=utf-8

import time


class Reader:
    f = None

    def __init__(self, fname=""):
        self.f = file(fname, "r")
        self.f.seek(0, 0)

    def getDate(self, timeStamp=1):
        timeArray = time.localtime(float(timeStamp))
        sdate = time.strftime("%Y-%m-%d", timeArray)
        shour = time.strftime("%H", timeArray)
        smin = time.strftime("%M", timeArray)
        return [sdate, shour, smin]

    def read(self):
        line = self.f.readline()
        r = line.split("/")
        if (len(r) < 8):
            return
        r[8] = r[8].replace("\n", "")
        [sdate, shour, smin] = self.getDate(int(r[0]))
        return {
            'time_tick': r[0],
            'sdate': sdate,
            'shour': shour,
            'ip': r[1],
            'device': r[2],
            'mac': r[3],
            'user': r[4],
            'app': r[5],
            'ver': r[6],
            'act': r[7],
            'content': r[8],
        }


if __name__ == '__main__':
    a = Reader().read()
    print a
