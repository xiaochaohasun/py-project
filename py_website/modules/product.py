#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,Blueprint,session
from mysql_connector import *

db=getDB()


blue_product=Blueprint('blue_product',__name__)


@blue_product.route('/product/list',methods=['GET','POST'])
def list():
    n,plist=db.query('select * from product')
    return render_template('product_list.html',products=plist,cname=session.get('cname'))


@blue_product.route('/product/detail/<id>',methods=['GET','POST'])
def product_detail(id):
    sql='select * from product where id=%s' % id
    p=db.queryOne(sql)
    print p
    return render_template('product_detail.html',product=p,cname=session.get('cname'))