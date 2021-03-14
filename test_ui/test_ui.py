# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 下午 5:43
@Auth ： Booker
@File ：test_ui.py
@IDE ：PyCharm
@Email: booker0318@163.com
"""
import pytest


class Test_demo3():
    @pytest.mark.run(order=1)
    @pytest.mark.smoke
    def test_three(self):
        print("testpytest文件包测试。。。1")
