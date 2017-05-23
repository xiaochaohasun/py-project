#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Blueprint

index=Blueprint('index',__name__)

@index.route('/')
@index.route('/index')
def index():
    return 'This is index page.<br><a href=/show_all>show more</a>'