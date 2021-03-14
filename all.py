# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 下午 5:38
@Auth ： Booker
@File ：all.py
@IDE ：PyCharm
@Email: booker0318@163.com
"""
import os
import pytest

if __name__ == '__main__':
    pytest.main()
    os.system('allure generate ./temp -o ./report --clean')
