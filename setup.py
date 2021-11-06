# -*- coding: utf-8 -*-
# !/usr/bin/env python3
"""
@author: zhuyuehui
@contact: zhuyuehui02@meituan.com
@time: 2021/11/6 12:58 下午
"""
import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyairwave",
    version="0.0.1",
    author="yuehui",
    author_email="zhuyuehui02@meituan.com",
    description="airwave8.0 简单API封装，",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/zhuyuehui1993/PyAirwave",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)

