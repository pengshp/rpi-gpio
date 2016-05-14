#!/usr/bin/env python
# -*- coding: utf-8 -*- 
__author__ = 'pengshp'

import RPi.GPIO as GPIO
import time

# BOARD编号方式，基于插座引脚编号
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()

#关闭警告
GPIO.setwarnings(False)

#设置管脚
GPIO.setup(11,GPIO.OUT)#11为输出
GPIO.setup(12,GPIO.IN)#12为输入

#初始化为高电平
GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

chan_list = [11,12]