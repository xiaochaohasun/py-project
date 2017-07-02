#!/usr/bin/python
# coding=utf-8

'''
输出程序将redis的数据导出，生成各种格式的报告
本文演示数据的提取和文本显示
'''

import cals.data_save_to_redis as ds
import json

cities = {}
provinces = {}
dates = {}
activeuser = {}


def getInfo():
    global cities, provinces
    for key in ds.getkeys("city*"):
        cities[key[len("city*"):]] = int(ds.get(key))

    for key in ds.getkeys("province*"):
        provinces[key[len("province*"):]] = int(ds.get(key))

    for key in ds.getkeys("access_by_date*"):
        dates[key[len("access_by_date*"):]] = int(ds.get(key))

    for key in ds.getkeys("user_active_by_date*"):
        activeuser[key[len("user_active_by_date*"):]] = int(ds.getSet(key))


def toTxt():
    getInfo()
    for key in cities.keys():
        print key, cities[key]
    for key in provinces.keys():
        print key, provinces[key]


def toExcel():
    import xlwt
    workbook = xlwt.Workbook(encoding='utf-8')
    sheet = workbook.add_sheet('aa', cell_overwrite_ok=True)
    getInfo()
    sheet.write(0, 0, "城市")
    sheet.write(0, 1, "访问次数")

    i = 1
    for key in cities.keys():
        print key, cities[key]
        sheet.write(i, 0, key)
        sheet.write(i, 1, cities[key])
        i = i + 1

    i = i + 1
    sheet.write(i, 0, "省份")
    sheet.write(i, 1, "访问次数")
    i = i + 1

    for key in provinces.keys():
        print key, provinces[key]
        sheet.write(i, 0, key)
        sheet.write(i, 1, provinces[key])
        i = i + 1

    workbook.save('report/report.xls')
    print '创建report.xls文件完成！'


def toHtmlBar():
    getInfo()
    f = open('report/template_bar.html')
    fout = open('report/bar_cities.html', 'w')
    try:
        s = f.read()
        s = s.replace("$zones", json.dumps(cities.keys()))
        s = s.replace("$counts", repr(cities.values()))
        fout.write(s)
    finally:
        f.close()
        fout.close()


def toHtmlCurve():
    getInfo()
    f = open('report/template_curve.html')
    fout = open('report/curve_user_by_date.html', 'w')
    try:
        s = f.read()
        s = s.replace("$title", "每日访问用户次数")
        s = s.replace("$date", json.dumps(dates.keys()))
        s = s.replace("$count", repr(dates.values()))
        fout.write(s)
    finally:
        f.close()
        fout.close()


def toHtmlCurve_foractive():
    getInfo()
    f = open('report/template_curve.html')
    fout = open('report/curve_active_user_by_date.html', 'w')
    try:
        s = f.read()
        s = s.replace("$title", "每人活跃用户")
        s = s.replace("$date", json.dumps(activeuser.keys()))
        s = s.replace("$count", repr(activeuser.values()))
        fout.write(s)
    finally:
        f.close()
        fout.close()


def toHtmlPie():
    getInfo()
    f = open('report/template_pie.html')
    fout = open('report/pei_province.html', 'w')
    data = []
    import json
    for key in provinces.keys():
        data.append([key, provinces[key]])
    try:
        s = f.read()
        ds = json.dumps(data)
        s = s.replace("$data", ds)
        fout.write(s)
    finally:
        f.close()
        fout.close()


def toAll():
    toTxt()
    toExcel()
    toHtmlBar()
    toHtmlPie()
    toHtmlCurve()
    toHtmlCurve_foractive()


if __name__ == "__main__":
    toAll()
