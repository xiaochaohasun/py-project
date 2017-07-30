import mysql.connector as MySQLdb


class DB_Class:
    __host = "localhost"
    __user = "root"
    __password = "qweRTY!23"
    __port = 3306
    __db = "pywebsite"
    __cn = None
    __cur = None

    def __init__(self, host, user, password, port, db):
        self.__host = host
        self.__user = user
        self.__password = password
        self.__port = port
        self.__db = db

        try:
            config = {
                'host': self.__host,
                'port': self.__port,
                'database': self.__db,
                'user': self.__user,
                'password': self.__password,
                'charset': 'utf8',
                'use_unicode': True,
                'get_warnings': True,
            }
            self.__cn = MySQLdb.connect(**config)
            self.__cur = self.__cn.cursor()
        except MySQLdb.Error, e:
            print "init error %d: %s" % (e.args[0], e.args[1])

    def usedb(self, db):
        try:
            self.__db = db
            self.__cn.select_db(db)
            self.__cur = self.__cn.cursor()
        except MySQLdb.Error, e:
            print "usedb error %d: %s" % (e.args[0], e.args[1])

    def query(self, sql):
        self.__cur = self.__cn.cursor()
        if (self.__cur == None):

            print "No connection or cursor!"
        else:
            count = self.__cur.execute(sql)
            if sql[:6] == "select":
                rows = self.__cur.fetchall()
                return len(rows), rows
            else:
                self.__cn.commit()
                return count, None

    def queryOne(self, sql):
        self.__cur = self.__cn.cursor()
        if (self.__cur == None):
            print "No connection or cursor!"
        else:
            count = self.__cur.execute(sql)
            return self.__cur.fetchone()


    def getMaxId(self, table, field):
        row = self.queryOne("select max(%s) from %s" % (field, table))
        return row[0]

class Data:
    db = None


def getDB():
    if Data.db == None:
        Data.db = DB_Class("localhost", "root", "qweRTY!23", 3306, "pywebsite")
    return Data.db

    # import tools.mysql_connector_DB as DB
    # db = DB.getDB()
