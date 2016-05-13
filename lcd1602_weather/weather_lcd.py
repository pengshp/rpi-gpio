#!/usr/bin/python
#
# HD44780 LCD Test Script for
# Raspberry Pi
#
# Author : Matt Hawkins
# Site   : http://www.raspberrypi-spy.co.uk
# Date   : 03/08/2012
# Edited : Matthew Manning
# Edited : 26/08/2012
#

# The wiring for the LCD is as follows:
# 1 : GND
# 2 : 5V
# 3 : Contrast (0-5V)*
# 4 : RS (Register Select)
# 5 : R/W (Read Write)       - GROUND THIS PIN
# 6 : Enable or Strobe
# 7 : Data Bit 0             - NOT USED
# 8 : Data Bit 1             - NOT USED
# 9 : Data Bit 2             - NOT USED
# 10: Data Bit 3             - NOT USED
# 11: Data Bit 4
# 12: Data Bit 5
# 13: Data Bit 6
# 14: Data Bit 7
# 15: LCD Backlight +5V**
# 16: LCD Backlight GND

#import
import RPi.GPIO as GPIO
import time

# Defind text to display
line1 = 'Newmarket'
line3 = 'Soham'
line5 = 'London'

# Define GPIO to LCD mapping
LCD_RS = 7
LCD_E  = 8
LCD_D4 = 25 
LCD_D5 = 24
LCD_D6 = 23
LCD_D7 = 18
LED_ON = 15

# Define some device constants
LCD_WIDTH = 16    # Maximum characters per line
LCD_CHR = True
LCD_CMD = False

LCD_LINE_1 = 0x80 # LCD RAM address for the 1st line
LCD_LINE_2 = 0xC0 # LCD RAM address for the 2nd line 

# Timing constants
E_PULSE = 0.00005
E_DELAY = 0.00005

def main():

  # Getting weather stats
  import urllib2
  import re
  ## curl -s "http://www.google.com/ig/api?weather=soham,uk" | sed's|.*<temp_c data="\([^"]*\)"/>.*|\1|'
  weatherURL1 = "http://www.google.com/ig/api?weather=newmarket,uk"
  weatherURL2 = "http://www.google.com/ig/api?weather=soham,uk"
  weatherURL3 = "http://www.google.com/ig/api?weather=london"
  
  response1 = urllib2.urlopen(weatherURL1)
  html1 = response1.read()
  response2 = urllib2.urlopen(weatherURL2)
  html2 = response2.read()
  response3 = urllib2.urlopen(weatherURL3)
  html3 = response3.read()
  
  #print html
  r_temp = re.compile("temp_c data=\"[0-9]{1,3}\"")
  
  temp_search1 = r_temp.search(html1)
  temp_search2 = r_temp.search(html2)
  temp_search3 = r_temp.search(html3)
  
  if temp_search1:
      temp1 = temp_search1.group(0)
      temp1 = re.sub("\D", "", temp1)
      line2 = temp1
      print temp1
  else:
	print "no temp found"
	line2 = "No temp found"

  if temp_search2:
      temp2 = temp_search2.group(0)
      temp2 = re.sub("\D", "", temp2)
      line4 = temp2
      print temp2
  else:
	print "no temp found"
	line4 = "No temp found"

  if temp_search3:
      temp3 = temp_search3.group(0)
      temp3 = re.sub("\D", "", temp3)
      line6 = temp3
      print temp3
  else:
	print "no temp found"
	line6 = "No temp found"
	  
  # Main program block

  GPIO.setmode(GPIO.BCM)       # Use BCM GPIO numbers
  GPIO.setup(LCD_E, GPIO.OUT)  # E
  GPIO.setup(LCD_RS, GPIO.OUT) # RS
  GPIO.setup(LCD_D4, GPIO.OUT) # DB4
  GPIO.setup(LCD_D5, GPIO.OUT) # DB5
  GPIO.setup(LCD_D6, GPIO.OUT) # DB6
  GPIO.setup(LCD_D7, GPIO.OUT) # DB7
  GPIO.setup(LED_ON, GPIO.OUT) # Backlight enable

  # Initialise display
  lcd_init()

  # Toggle backlight on
  GPIO.output(LED_ON, True)
  time.sleep(1)

  # Send first location temperature
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string(line1,2)
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string(line2,2)

  time.sleep(3) # 3 second delay

  # Send second location temperature
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string(line3,2)
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string(line4,2)

  time.sleep(3) # 3 second delay

  # Send Thrid location temperature
  lcd_byte(LCD_LINE_1, LCD_CMD)
  lcd_string(line5,2)
  lcd_byte(LCD_LINE_2, LCD_CMD)
  lcd_string(line6,2)

  time.sleep(30)

def lcd_init():
  # Initialise display
  lcd_byte(0x33,LCD_CMD)
  lcd_byte(0x32,LCD_CMD)
  lcd_byte(0x28,LCD_CMD)
  lcd_byte(0x0C,LCD_CMD)  
  lcd_byte(0x06,LCD_CMD)
  lcd_byte(0x01,LCD_CMD)  

def lcd_string(message,style):
  # Send string to display
  # style=1 Left justified
  # style=2 Centred
  # style=3 Right justified
  
  if style==1:
    message = message.ljust(LCD_WIDTH,)  
  elif style==2:
    message = message.center(LCD_WIDTH,)
  elif style==3:
    message = message.rjust(LCD_WIDTH,)

  for i in range(LCD_WIDTH):
    lcd_byte(ord(message[i]),LCD_CHR)

def lcd_byte(bits, mode):
  # Send byte to data pins
  # bits = data
  # mode = True  for character
  #        False for command

  GPIO.output(LCD_RS, mode) # RS

  # High bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x10==0x10:
    GPIO.output(LCD_D4, True)
  if bits&0x20==0x20:
    GPIO.output(LCD_D5, True)
  if bits&0x40==0x40:
    GPIO.output(LCD_D6, True)
  if bits&0x80==0x80:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY)      

  # Low bits
  GPIO.output(LCD_D4, False)
  GPIO.output(LCD_D5, False)
  GPIO.output(LCD_D6, False)
  GPIO.output(LCD_D7, False)
  if bits&0x01==0x01:
    GPIO.output(LCD_D4, True)
  if bits&0x02==0x02:
    GPIO.output(LCD_D5, True)
  if bits&0x04==0x04:
    GPIO.output(LCD_D6, True)
  if bits&0x08==0x08:
    GPIO.output(LCD_D7, True)

  # Toggle 'Enable' pin
  time.sleep(E_DELAY)    
  GPIO.output(LCD_E, True)  
  time.sleep(E_PULSE)
  GPIO.output(LCD_E, False)  
  time.sleep(E_DELAY)   

if __name__ == '__main__':
  main()

