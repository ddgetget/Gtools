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

from gtools.config import xml_dict_data, dict_data, xml_dict_data1
from gtools.data.transformer.xml import dict_xml, xml_dict
from gtools.io.json import write_json_line, read_json_line, read_json, write_json
from gtools.io.xml import write_xml_by_json
from gtools.io.yaml import write_yaml, read_yaml


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


if __name__ == '__main__':
    if not os.path.exists("temp"):
        os.mkdir("temp")

    test_json(data=dict_data)
    test_yaml(dict_data)

    write_xml_by_json(path="temp/data.xml", data=xml_dict_data)
    write_xml_by_json(path="temp/data.xml", data=xml_dict_data1)

    xmlstr = dict_xml(data=xml_dict_data)
    print(xmlstr)
    print(type(xmlstr))
    dict = xml_dict(xmlstr=xmlstr, moudle="mydocument")
    print(dict["mydocument"]["and"])
