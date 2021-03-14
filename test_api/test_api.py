# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/14 下午 12:31
@Auth ： Booker
@File ：test_api.py
@IDE ：PyCharm
@Email: booker0318@163.com
"""
import pytest
from test_yaml.yaml_util import Yaml_util
import yaml
import requests
import os


class Test_Api():
    @pytest.mark.parametrize('args', Yaml_util('/test_data.yaml').read_yaml())
    def test_one_api(self, args):
        url = args['api_requests']['url']
        res = requests.get(url)
        print(res.status_code)

        print(args)
