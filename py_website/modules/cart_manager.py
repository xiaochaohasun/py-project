#!/bin/python
# coding=utf8
import json
import time

from flask import session

from mysql_connector import *
db = getDB()


class cart_manager:
    items = []

    def __init__(self):
        self.items = session.get("__items")
        if not self.items:
            session["__items"] = self.items = []

    def find(self, pid):
        for item in self.items:
            if item['pid'] == pid:
                return item

    def add_product(self, pid, pcount):
        pid = int(pid)
        pcount = int(pcount)
        item = self.find(pid)
        if item:
            item['pcount'] = item['pcount'] + pcount
            item['total'] = float(item['price']) * float(item['pcount'])
        else:
            sql = "select * from product where id='%s'" % (pid)
            n, rows = db.query(sql)
            price = float(rows[0][4])
            total = float(pcount) * price
            pname = rows[0][1]
            pic = rows[0][3]
            self.items.append(
                    {"pid": pid, "pname": pname, "pcount": pcount, "price": price, "total": total, "pic": pic})
        session["__items"] = self.items #修改完集合后,必须重新放入session,说明从session取值,是复制不是引用

        return len(self.items)

    def del_product(self, pid):
        pid = int(pid)
        item = self.find(pid)
        self.items.remove(item)
        session["__items"] = self.items
        return len(self.items)

    def total(self):
        sum = 0.0
        for item in self.items:
            sum += item['total']
        return str(sum)

    def getItems(self):
        return self.items

    def size(self):
        return str(len(self.items))

    def bill(self):
        n = len(self.items)
        if n > 0:
            bid = int(db.getMaxId("bill", "id")) + 1
            uid = session["uid"]
            if not uid:
                return "交易已经过期,请重新选购商品!"
            dtime = time.strftime('%Y-%m-%d %H:%M:%S')
            totalpay = self.total()
            sql = "insert into bill value('%s','%s','%s','%s')" % (bid, uid, totalpay, dtime)
            db.query(sql)
            # return "交易成功!交易单号:%s" % bid
            strs={"str":"true","billnum":bid}
            return json.dumps(strs)

if __name__ == "__main__":
    c = cart_manager()
    c.add_product(1, 2)
    c.add_product(1, 3)
    c.add_product(2, 3)
    c.del_product(1)
    print c.getItems()
