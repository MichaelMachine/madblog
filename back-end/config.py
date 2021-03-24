#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ---
# @Author: Michael
# @Software: Pycharm
# @file: config.py
# @Time: 2021/3/24 6:05 下午
# ---
import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'), encoding='utf-8')


class Config:
    pass
