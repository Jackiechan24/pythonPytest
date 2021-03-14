# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 下午 5:32
@Auth ： Booker
@File ：test_two.py
@IDE ：PyCharm
@Email: booker0318@163.com
"""

import pytest
import time

class Test_demo2():
    @pytest.mark.smoke2
    def test_two2(self):
        # time.sleep(2)
        print("第二个测试。。。")
