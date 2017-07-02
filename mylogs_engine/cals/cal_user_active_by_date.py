#!/usr/bin/python
# coding=utf-8

"""
将IP地址翻译为具体地名
这里使用的是假的地名,真实情况,可以通过:
1)自己建立的地址库
2)网络上的开放地址库进行翻译
http://ip.taobao.com/service/getIpInfo.php?ip=120.25.63.167
http://ip.ws.126.net/ipquery?ip=120.25.63.167
"""
import data_save_to_redis as db


def cal(log, parameters=[]):
    db.addSet("user_active_by_date=" + log['sdate'], log['user'])
