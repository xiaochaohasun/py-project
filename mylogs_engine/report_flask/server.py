#!/bin/python
# coding=utf8
import json

from flask import Flask, render_template

app = Flask(__name__, template_folder='views', static_url_path='', static_folder='')

import redis
import data_save_to_redis as ds


def getInfo():
    cities = {}
    provinces = {}
    dates = {}
    activeuser = {}

    for key in ds.getkeys("city*"):
        cities[key[len("city*"):]] = int(ds.get(key))

    for key in ds.getkeys("province*"):
        provinces[key[len("province*"):]] = int(ds.get(key))

    for key in ds.getkeys("access_by_date*"):
        dates[key[len("access_by_date*"):]] = int(ds.get(key))

    for key in ds.getkeys("user_active_by_date*"):
        activeuser[key[len("user_active_by_date*"):]] = int(ds.getSet(key))

    return cities, provinces, dates, activeuser


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/bar')
def bar():
    cities, provinces, dates, activeuser = getInfo()
    zones = json.dumps(cities.keys())
    counts = repr(cities.values())
    return render_template('bar.html', zones=zones, counts=counts)

@app.route('/pie')
def pie():
    data=[]
    cities, provinces, dates, activeuser = getInfo()
    for key in provinces.keys():
        data.append([key, provinces[key]])
    data = json.dumps(data)
    return render_template('pie.html', data=data)

@app.route('/curve')
def curve():
    cities, provinces, dates, activeuser = getInfo()
    title=json.dumps('每人活跃用户')
    data=json.dumps(activeuser.keys())
    count= json.dumps(activeuser.values())
    print data,count
    return render_template('curve.html', data=data,count=count,title=title)



if __name__ == '__main__':
    app.run(debug=True)