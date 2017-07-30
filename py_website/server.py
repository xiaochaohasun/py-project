#!/usr/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,render_template
from modules.user import blue_user
from modules.product import blue_product
from modules.cart import blue_cart
from modules.bill import blue_bill

app = Flask(__name__, template_folder="views", static_url_path='', static_folder='')
app.config["SECRET_KEY"] = "test"

app.register_blueprint(blue_user)
app.register_blueprint(blue_product)
app.register_blueprint(blue_cart)
app.register_blueprint(blue_bill)

if __name__ == '__main__':
    app.run(debug=True, port=4000, host="0.0.0.0", threaded=True)
