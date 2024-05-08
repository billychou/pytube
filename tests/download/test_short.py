#!/usr/bin/env python3
# -*- coding:utf-8 -*-
"""
File: test_short.py
Author: 提昂(zsc1528@gmail.com)
Date: 2024/5/8 17:51
Copyright: 三分地信息技术有限公司
"""
from pytube import YouTube


def test_download_shorts():
    url = "https://www.youtube.com/shorts/ed8OoSndEWc"
    # ret = YouTube(url).streams.first().download()
    youtube = YouTube(url)
    streams = youtube.streams
    ret = streams.first().download()
    print(ret)

