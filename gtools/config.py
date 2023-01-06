#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2023-01-06 17:35
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    config.py
# @Project: FastDeploy
# @Package: 
# @Ref:
xml_dict_data = {
    "mydocument": {
        "@has": "an attribute",
        "and": {
            "many": [
                "elements",
                "more elements"
            ]
        },
        "plus": {
            "@a": "complex",
            "#text": "element as well"
        }
    }
}

xml_dict_data1 = {
    "mydocument": {
        "@has": "an attribute",
        "and": {
            "many": [
                "elements",
                "more elements"
            ]
        },
        "plus": {
            "@a": "complex",
            "#text": "element as well"
        },
        "mydocument": {
            "@has": "an attribute",
            "and": {
                "many": [
                    "elements",
                    "more elements"
                ]
            },
            "plus": {
                "@a": "complex",
                "#text": "element as well"
            },

        }
    }
}

dict_data = {
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
