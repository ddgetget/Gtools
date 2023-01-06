#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2023-01-06 16:02
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    json.py
# @Project: FastDeploy
# @Package: 
# @Ref:
import json

from jsonlines import jsonlines


def write_json(path, data):
    """
    将字典数据一json形式写到本地
    :param path: json数据路径
    :param data: 字典数据
    :return: None
    """
    json_str = json.dumps(data, indent=2, ensure_ascii=False)
    with open(path, 'w', encoding='utf-8') as json_file:
        json_file.write(json_str)


def read_json(path):
    """
    读取本地json数据到字典
    :param path: josn数据路径
    :return: 返回字典
    """
    with open(path, 'r', encoding="utf-8") as load_f:
        load_dict = json.load(load_f)
    return load_dict


def write_json_line(path, data):
    """
    按行写json文件
    :param path: 写文件路径
    :param data: 列表嵌套字典数据 [{},{}...]
    :return: None
    """

    file = jsonlines.open(path, "w")
    for item in data:
        jsonlines.Writer.write(file, item)  # 每行写入一个dict


def read_json_line(path):
    """
    读取jsonline是数据
    :param path: 数据路径
    :return: 列表嵌套字典数据 [{},{}...]
    """
    # 读文件，不使用jsonlines.open() 而是直接open()
    file = open(path, "r", encoding='utf-8')
    result = []
    reader = jsonlines.Reader(file)
    for each in reader:
        result.append(each)
    return result
