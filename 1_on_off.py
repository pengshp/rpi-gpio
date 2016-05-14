#!/usr/bin/env python
# -*- coding: utf-8 -*- 
__author__ = 'pengshp'

import RPi.GPIO as GPIO
import time

# 设置管脚编号模式为BOARD
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()

#关闭警告
GPIO.setwarnings(False)

#设置输入和输出
GPIO.setup(11,GPIO.OUT)#
GPIO.setup(12,GPIO.IN)#

#初始化引脚为高电平
GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

chan_list = [11,12]
