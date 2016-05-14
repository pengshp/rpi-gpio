#!/usr/bin/env python
# -*- coding: utf-8 -*- 
__author__ = 'pengshp'

import RPi.GPIO as GPIO
import time
#¿¿¿
# BOARD±àºÅ·½Ê½£¬»ùÓÚ²å×ùÒı½Å±àºÅ
GPIO.setmode(GPIO.BOARD)
mode = GPIO.getmode()

#¹Ø±Õ¾¯¸æ
GPIO.setwarnings(False)

#ÉèÖÃ¹Ü½Å
GPIO.setup(11,GPIO.OUT)#11ÎªÊä³ö
GPIO.setup(12,GPIO.IN)#12ÎªÊäÈë

#³õÊ¼»¯Îª¸ßµçÆ½
GPIO.setup(channel, GPIO.OUT, initial=GPIO.HIGH)

chan_list = [11,12]
