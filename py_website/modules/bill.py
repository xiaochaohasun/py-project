#!/bin/python
# coding=utf8
import time

from flask import Blueprint, request, session
from cart_manager import cart_manager

blue_bill = Blueprint('bule_bill', __name__)


@blue_bill.route('/bill/add',methods=['GET','POST'])
def bill_add():
    cm=cart_manager()
    return cm.bill()


@blue_bill.route('/bill/list',methods=['GET','POST'])
def bill_list():
    return "bill_list"
