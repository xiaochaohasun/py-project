#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Blueprint

show_all=Blueprint('show_all',__name__)

@show_all.route('/show_all')
def show_all():
    return 'This is show all page.'