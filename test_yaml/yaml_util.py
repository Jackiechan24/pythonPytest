# -*- coding: utf-8 -*-
"""
@Time ： 2021/3/13 下午 10:09
@Auth ： Booker
@File ：yaml_util.py
@IDE ：PyCharm
@Email: booker0318@163.com
"""
import yaml


class Yaml_util():
    def __init__(self, yaml_file):
        self.yaml_file = yaml_file

#读取yaml文件
    def read_yaml(self):
        with open(self.yaml_file, encoding='utf-8') as f:
            data = yaml.load(f, Loader=yaml.FullLoader)
            return data


if __name__ == '__main__':
    Yaml_util('test_data.yaml').read_yaml()
