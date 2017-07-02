#!/usr/bin/python
# coding=utf-8

import importlib
import sys
sys.path.append("..")

import report_output as output
from logs_reader import Reader

# 定义了计算单元及参数
chains = [
    ['cal_access_by_date', []],
    ['cal_ip_converter',[]],
    ['cal_user_active_by_date',[]],
    ['cal_simple_counter',['device']],
    ['cal_simple_counter', ['act']],
    ['cal_simple_counter', ['app', 'ver']],

]
for key in chains:
    key.append(importlib.import_module("cals.%s" % key[0]))

input = Reader("data/standard/std_user_behavior.log")
i = 1
while True:
    i += 1
    print i
    log = input.read()
    if (log == None):
        break;
    for j in chains:
        j[2].cal(log, j[1])

#output.toAll()
