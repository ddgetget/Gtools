#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2023-01-06 17:34
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    xml.py
# @Project: FastDeploy
# @Package: 
# @Ref:
import xmltodict


def dict_xml(data):
    """
    dict转xml
    dictstr: dict字符串
    return: xml字符串
    """
    xmlstr = xmltodict.unparse(data, pretty=True)
    return xmlstr


def xml_dict(xmlstr, moudle):
    """
    xml转dict
    xmlstr: xml字符串
    moudle:根节点
    return: dict字符串
    """
    data = xmltodict.parse(xmlstr, process_namespaces=True)
    dictdata = dict(data)
    _dictdata = dict(dictdata[moudle])
    dictdata[moudle] = _dictdata
    return dictdata
