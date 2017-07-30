#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,Blueprint,redirect, session
from mysql_connector import *
import json
from cart_manager import cart_manager

db=getDB()


blue_cart=Blueprint('blue_cart',__name__)


@blue_cart.route('/cart/add',methods=['GET','POST'])
def cart_add():
    pid=request.values.get('pid')
    pcount=request.values.get('pcount')

    cm = cart_manager()
    cm.add_product(pid, int(pcount));

    print cm.getItems()
    print cm.size()
    strs={"str":"true","pcount":cm.size()}
    return json.dumps(strs)

@blue_cart.route('/cart/list')
def cart_list():
    cm = cart_manager()
    rows = cm.getItems()
    total = cm.total()
    return render_template("cart_list.html", rows=rows, total=total,cname=session.get('cname'))


@blue_cart.route('/cart/del')
def cart_del():
    pid = request.values.get("pid");
    cm = cart_manager()
    cm.del_product(pid)
    return redirect("/cart/list")

