# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 下午 5:20
@Auth ： booker
@File ：test_one.py
@IDE ：PyCharm

"""
import pytest
import time


class Test_demo1():
    @pytest.mark.run(order=2)
    def test_one1(self):
        print("第一个测试。。。")
    @pytest.mark.run(order=1)
    def ootest_one2(self):
        print("第二个测试。。。")
        assert 1 == 3
    @pytest.mark.smoke
    def test_one3(self):
        print("第三个测试。。。")

    def test_one4(self):
        print("第四个测试。。。")
