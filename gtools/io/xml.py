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

from xml.etree import ElementTree as et


def write_xml(path, data):
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

    # 创建根标签
    root = et.Element('home')
    # 创建子标签大儿子
    son1 = et.SubElement(root, 'son', attrib={'name': 'son01'})
    # 创建小儿子
    son2 = et.SubElement(root, 'son', attrib={'name': 'son02'})

    # 在大儿子中创建孙子
    gdson = et.SubElement(son1, 'gdson', attrib={'name': 'gdson1'})

    # 把root节点放到根节点
    tree = et.ElementTree(root)
    # 保存xml
    tree.write(path, encoding='utf-8')


def read_xml(path):
    """
    读取本地json数据到字典
    :param path: josn数据路径
    :return: 返回字典
    """
    f = open(path, 'r', encoding="utf-8")  # 读取文件
    yml_config = yaml.load(f, Loader=yaml.FullLoader)  # Loader为了更加安全
    """Loader的几种加载方式
    BaseLoader - -仅加载最基本的YAML
    SafeLoader - -安全地加载YAML语言的子集。建议用于加载不受信任的输入。
    FullLoader - -加载完整的YAML语言。避免任意代码执行。这是当前（PyYAML5.1）默认加载器调用yaml.load(input)（发出警告后）。
    UnsafeLoader - -（也称为Loader向后兼容性）原始的Loader代码，可以通过不受信任的数据输入轻松利用。"""
    return yml_config
