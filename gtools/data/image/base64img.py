#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time:    2023-01-09 16:33
# @Author:  geng
# @Email:   yonglonggeng@163.com
# @WeChat:  superior_god
# @File:    base64img.py
# @Project: RemotePatrolServer
# @Package: 
# @Ref:
import base64
import os


def image2base64(path):
    with open(path, "rb") as f:  # 转为二进制格式
        base64_data = base64.b64encode(f.read())  # 使用base64进行加密

        # img_base64=(str(base64_data, encoding="utf-8"))
        img_base64 = base64_data.decode('utf-8')
    return img_base64


def base642image(img_base64, path):
    image_data = base64.b64decode(img_base64)
    with open(path, 'wb') as f:
        f.write(image_data)  # 打开路径将结果写入到文件中
