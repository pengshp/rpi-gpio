#!/usr/bin/env python
# -*- coding: utf-8 -*- 
__author__ = 'pengshp'

import RPi.GPIO as GPIO
import time

# BOARD��ŷ�ʽ�����ڲ������ű��
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()

#�رվ���
GPIO.setwarnings(False)

#���ùܽ�
GPIO.setup(11,GPIO.OUT)#11Ϊ���
GPIO.setup(12,GPIO.IN)#12Ϊ����

#��ʼ��Ϊ�ߵ�ƽ
GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

chan_list = [11,12]