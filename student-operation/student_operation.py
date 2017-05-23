#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask, request, render_template, url_for, redirect

import mysql_db_connector as DB

db = DB.getDB()

import sys

reload(sys)
sys.setdefaultencoding('utf8')

app = Flask(__name__,static_url_path='/res', static_folder='/http_resource')
app.config["SECRET_KEY"] = "test"


@app.route('/')
@app.route('/list')
def show_student_list():
    count, stues = db.query('select * from student')
    return render_template('list_student.html', stues=stues)


@app.route('/edit_student/<id>')
def edit_student(id):
    stu = (id, '', '')
    print id
    if int(id) != 0:
        stu = db.queryOne('select * from student where id=%s' %id)
        print stu
    return render_template('edit_student.html', stu=stu)


@app.route('/del_student/<id>')
def del_student(id):
    sql = 'delete from student where id=%s' % id
    db.query(sql)

    return show_student_list()


@app.route('/save_student', methods=['GET', 'POST'])
def save_student():
    id = request.values.get("id")
    xm = request.values.get("xm")
    age = request.values.get("age")
    print "idddd=", id
    if int(id) != 0:
        sql = "update student set xm='%s', age='%s' where id='%s'" % (xm, age, id)
    else:
        row = db.queryOne("select max(id) from student")
        maxid = int(row[0]) + 1
        sql = "insert into student values('%s','%s','%s')" % (maxid, xm, age)
    print sql
    db.query(sql)
    #return redirect(url_for("list"))
    return redirect('/list')


if __name__ == '__main__':
    app.run(debug=True)
