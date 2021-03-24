#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---
# @Author: Michael
# @Software: Pycharm
# @file: ping.py
# @Time: 2021/3/24 6:02 下午
# ---
from flask import jsonify
from app.api import bp


@bp.route('/ping', methods=['GET'])
def ping():
    '''前端 Vue.js 用来测试与后端Flask API 的连通性'''
    return jsonify('PONG!')
