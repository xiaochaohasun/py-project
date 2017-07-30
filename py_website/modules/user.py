#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,request,render_template,Blueprint,redirect, session
from mysql_connector import *

db=getDB()


blue_user=Blueprint('blue_user',__name__)


@blue_user.route('/',methods=['GET','POST'])
def login():
    second=request.values.get('second')
    print second
    if second == None:
        msg=''
        return render_template('login.html',msg=msg)
    else:
        cname=request.values.get('cname')
        cpwd=request.values.get('cpwd')

        sql="select * from user where cname='%s' and cpwd='%s' " %(cname,cpwd)

        n,rows=db.query(sql)
        if n == 1:
            session["uid"]=rows[0][0]
            session['cname']=cname
            return redirect('product/list')
        else:
            msg='login or passwd is wrong!'
            return render_template('login.html',msg=msg)


@blue_user.route('/regist')
def login_regist():
    cname = request.values.get("cname");
    cpwd = request.values.get("cpwd");
    cpwd2 = request.values.get("cpwd2");

    if cpwd != cpwd2:
        return render_template("regist.html", msg=u"密码不一致!")

    n, rows = db.query("select * from user where cname='%s' and cpwd='%s'" % (cname, cpwd))
    if n == 1 & n > 1:
        return render_template("regist.html", msg=u"登陆名称已经存在,请换个名称!")
    else:
        mid = db.getMaxId("user", "id")
        uid = int(mid) + 1
        sql = "insert INTO user VALUES ('%d','%s','%s')" % (uid, cname, cpwd)
        print sql
        db.query(sql)

        return render_template("login.html", msg=u"请登陆")


