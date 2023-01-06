#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2023-01-06 16:49
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    xml.py
# @Project: FastDeploy
# @Package: 
# @Ref: https://www.jb51.net/article/259852.htm
import json
from xml.etree import ElementTree as ET

import xmltodict


def init_xml(path):
    pass


def write_xml(path, ann_tree):
    """
    将字典数据一json形式写到本地
    :param path: json数据路径
    :param data: 字典数据
    :return: None
    <?xml version="1.0" encoding="utf-8"?>
    <catalog>
        <maxid>aaa</maxid>
        <login username="test" passwd='123456'>
            <caption>PythonTest</caption>
            <item >
                <caption>测试XML</caption>
            </item>
        </login>
        <item >
            <caption>cat</caption>
        </item>
    </catalog>
    """
    ann_tree.write(path, encoding="utf-8")


def write_xml_by_json(path, data):
    """
    数据需要有一个根节点
    :param path:
    :param data:
    :return:
    example: {'student': {'course': {'name': 'math', 'score': '90'},
                        'info': {'sex': 'male', 'name': 'name'}, 'stid': '10213'}}
    """
    xmlstr = xmltodict.unparse(data)
    # print(xmlstr, type(xmlstr))
    with open(path, 'w', encoding="utf-8") as f:
        f.write(xmlstr)


def read_xml(path):
    """
    读取本地json数据到字典
    :param path: josn数据路径
    :return: 返回字典
    """
    ann_tree = ET.parse(path)
    ann_root = ann_tree.getroot()
    return ann_root
