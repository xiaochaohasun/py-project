#!/usr/bin/env python
#-*- coding:utf-8 -*-

from flask import Flask
from index import index
from show_all import show_all

app = Flask(__name__)
app.register_blueprint(index)
app.register_blueprint(show_all)


if __name__ == "__main__":
    app.run(debug=True)
