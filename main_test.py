#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2023-01-06 16:03
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    main_test.py
# @Project: FastDeploy
# @Package: 
# @Ref:
import os.path

from gtools.io.json import write_json_line, read_json_line, read_json, write_json
from gtools.io.xml import write_xml
from gtools.io.yaml import write_yaml, read_yaml

data = {
    "sentence": "新疆按问安静的空间和凯撒好",
    "extracted": [
        {
            "subject": "美国",
            "trigger": "打击",
            "object": "日本"
        },
        {
            "subject": "台独",
            "trigger": "前往",
            "object": "大陆"
        }
    ],
    "time": 202012010
}


def test_json(data):
    write_json("temp/data.json", data)
    write_json_line(path="temp/json_line.json", data=[data, data])
    result = read_json_line(path="temp/json_line.json")
    print(result)
    result = read_json(path="temp/data.json")
    print(result)


def test_yaml(data):
    write_yaml(path="temp/data.yml", data=data)
    result = read_yaml(path="temp/data.yml")
    print(result)


def test_xml(data):
    write_xml(path="temp/data.xml", data=data)


if __name__ == '__main__':
    if not os.path.exists("temp"):
        os.mkdir("temp")

    # test_json()
    # test_yaml(data)
    test_xml(data)
