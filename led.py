#!/usr/bin/env python
# -*- coding: utf-8 -*- 
__author__ = 'pengshp'

import RPi.GPIO as GPIO
import time

# BOARD编号方式，基于插座引脚编号
GPIO.setmode(GPIO.BOARD)
# 输出模式
GPIO.setup(11,GPIO.OUT)
i=10
while i > 0:
	GPIO.output(11,True) #True=GPIO.HIGH=1
	time.sleep(1)
	GPIO.output(11,0)    #False=GPIO.LOW=0
	time.sleep(1)
	i-=1
GPIO.cleanup() # 退出时清除管脚电平
