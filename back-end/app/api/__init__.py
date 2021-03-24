#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---
# @Author: Michael
# @Software: Pycharm
# @file: __init__.py
# @Time: 2021/3/24 5:59 下午
# ---
from flask import Blueprint

bp = Blueprint('api', __name__)

# 写在最后为了防止循环导入，ping.py 文件也会导入 bp
from app.api import ping
