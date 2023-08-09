#!/usr/bin/env python

# Piclockmatrix
# by superjulien 
# > https://github.com/Superjulien
# > https://framagit.org/Superjulien
# V0.10

####### Lcd + bouton
import I2C_LCD_driver
import RPi.GPIO as GPIO
import time
import sys

####### Matrix
import re
import time
import argparse

from luma.led_matrix.device import max7219
from luma.core.interface.serial import spi, noop
from luma.core.render import canvas
from luma.core.virtual import viewport
from luma.core.legacy import text, show_message
from luma.core.legacy.font import proportional, CP437_FONT, TINY_FONT, SINCLAIR_FONT, LCD_FONT

###### IP show
import socket
import os

###### Weather

from pyowm.owm import OWM
from pyowm.utils.config import get_default_config
from pyowm.utils import timestamps

#Setting :
lang = 'EN'
city = 'City,EN'
key = 'api-key'

####### Options Matrix
serial = spi(port=0, device=0, gpio=noop())
device = max7219(serial, cascaded=3, block_orientation=0, rotate=0, blocks_arranged_in_reverse_order=False)

###### GPIO Set
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP) # UP
GPIO.setup(27, GPIO.IN, pull_up_down=GPIO.PUD_UP) # DOWN
GPIO.setup(24, GPIO.IN, pull_up_down=GPIO.PUD_UP) # RST
GPIO.setup(23, GPIO.IN, pull_up_down=GPIO.PUD_UP) # Select
GPIO.setup(22, GPIO.IN, pull_up_down=GPIO.PUD_UP) # LEFT
GPIO.setup(18, GPIO.IN, pull_up_down=GPIO.PUD_UP) # RIGHT


# LCD set
lcd = I2C_LCD_driver.lcd()

# set global timer
timer = 0
sub_menu = 0
refresh = 0
# set global O'clock
reseter = 0
# set global variables used
update = 1 # causes LCD to be updated while set to 1
mlevel = 1 # current menu level
blevel = 1 # last menu level

# Timer
import time
def countdown(p,q):
    i=p
    j=q
    k=0
    while True:
        if(j==-1):
            j=59
            i -=1
        if(j > 9):
            print(str(k)+str(i)+":"+str(j), end="\r")
        else:
            print(str(k)+str(i)+":"+str(k)+str(j), end="\r")
        time.sleep(1)
        j -= 1
        if(i==0 and j==-1):
            break
    if(i==0 and j==-1):
        print("Goodbye!", end="\r")
        time.sleep(1)

# Body
def startup():
    lcd.lcd_display_string("**** START ****", 1)
    time.sleep(1)

def level1():
    #main menu
    lcd.lcd_display_string("Selection", 1)
    lcd.lcd_display_string(">> Up or Down <<", 2)

def level2():
    #sub menu
    lcd.lcd_display_string("Selection", 1)
    lcd.lcd_display_string(">> Info&Date  <<", 2)

def level3():
    #sub menu
    lcd.lcd_display_string("Selection", 1)
    lcd.lcd_display_string(">>   Weather    <<", 2)

def level4():
    #sub menu
    lcd.lcd_display_string("Selection", 1)
    lcd.lcd_display_string(">>   *******  <<", 2)

def level5():
    #sub menu
    lcd.lcd_display_string("Selection", 1)
    lcd.lcd_display_string(">> Countdown  <<", 2)

def level6():
    #sub menu
    lcd.lcd_display_string("Selection", 1)
    lcd.lcd_display_string(">>   Watch    <<", 2)

def level7():
    #sub menu
    lcd.lcd_display_string("Selection", 1)
    lcd.lcd_display_string(">> Stopwatch  <<", 2)

def select_level1():
    gw = os.popen("ip -4 route show default").read().split()
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect((gw[2], 0))
    ipaddr = s.getsockname()[0]
    gateway = gw[2]
    host = socket.gethostname()
    msg = (ipaddr + " " + host)
    msg2 = str(msg)
    show_message(device, msg2, fill="white", font=proportional(CP437_FONT),scroll_delay=0.2)
    msg = time.strftime('%d/%m/%Y %H:%M:%S')
    msg2 = str(msg)
    show_message(device, msg2, fill="white", font=proportional(CP437_FONT),scroll_delay=0.2)
    time.sleep(1)

def select_level2():
    global lang, city, key
    config_dict = get_default_config()
    config_dict['language'] = lang
    owm = OWM(key, config_dict)
    mgr = owm.weather_manager()
    obser = mgr.weather_at_place(city)
    weather = obser.weather
    status = weather.detailed_status
    hum = weather.humidity
    sunrise_date = weather.sunrise_time(timeformat='date')
    sunrset_date = weather.sunset_time(timeformat='date')
    wind_dict_in_meters_per_sec = obser.weather.wind()
    wind_dict_in_meters_per_sec['speed']
    temp_dict_kelvin = weather.temperature()
    temp_dict_kelvin['temp_min']
    temp_dict_kelvin['temp_max']
    temp_dict_celsius = weather.temperature('celsius')
    h = int(time.strftime("%H"))
    h = h - 7
    three_h_forecaster = mgr.forecast_at_place(city, '3h')
    tomorrow = timestamps.tomorrow(h,0)
    weath = three_h_forecaster.get_weather_at(tomorrow)
    status2 = weath.detailed_status
    temp_dict_kelvin2 = weath.temperature()
    temp_dict_celsius2 = weath.temperature('celsius')
    meteo = str(str(temp_dict_celsius['temp'])+"C "+str(status).replace('é','e').replace('è','e')+" "+str(temp_dict_celsius['feels_like'])+"C +"+str(temp_dict_celsius['temp_max'])+"C -"+str(temp_dict_celsius['temp_min'])+"C Hum:"+ str(hum)+"% Wind:"+str(wind_dict_in_meters_per_sec['speed']) +"m/s "+"Sun:"+str(sunrise_date.strftime('%H:%M:%S'))+" - "+str(sunrset_date.strftime('%H:%M:%S'))+" || Tomorrow at "+str(h)+"h : "+str(temp_dict_celsius2['temp'])+"C "+str(status2).replace('é','e').replace('è','e')+" "+str(temp_dict_celsius2['feels_like'])+"C")
    show_message(device, meteo, fill="white", font=proportional(CP437_FONT),scroll_delay=0.1)

def select_level3():
    msg =""

def select_level4():
    global sub_menu, refresh
    sub_menu = 1
    lcd.lcd_clear()
    while True :
        while update ==1:
            time.sleep (0.1)
            lcd.lcd_clear()
        lcd.lcd_display_string("Select time : ", 1)
        lcd.lcd_display_string(str(timer), 2)
        refresh = 0
        if sub_menu == 0 :
            break

def select_level5():
    while True :
        global reseter
        if reseter == 1 :
            msg = "<<>>"
            show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT),scroll_delay=0.1)
            reseter = 0
            break
        msg = time.strftime('%H:%M')
        msg2 = str(msg)
        with canvas(device) as draw:
            text(draw, (4, 1), msg2, fill="white",font=proportional(TINY_FONT))
        time.sleep(1)

def select_level6():
    global reseter
    second = 0
    minute = 0
    hours = 0
    while True :
        global reseter
        if reseter == 1 :
            msg = "<<>>"
            show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT),scroll_delay=0.1)
            reseter = 0
            break
        msg = [hours,minute,second]
        msg = str(msg).replace(" ","").replace('[','').replace(']','')
        with canvas(device) as draw:
            text(draw, (1, 1), msg, fill="white",font=proportional(TINY_FONT))
        time.sleep(1)
        second+=1
        if(second == 60):
            second = 0
            minute+=1
        if(minute == 60):
            minute = 0
            hour+=1;

def left(channel):
    global timer, refresh
    timer -=1
    if timer < 0: timer = 0
    refresh = 1

def right(channel):
    global timer, refresh
    timer +=1
    refresh = 1

def up(channel):
    global mlevel, update, blevel
    blevel = mlevel
    mlevel = mlevel + 1
    if mlevel > 7: mlevel = 1 #error checking
    update = 1

def down(channel):
    global mlevel, update, blevel
    blevel = mlevel
    mlevel = (mlevel) - 1
    if mlevel == 0: mlevel = 7
    if mlevel > 7: mlevel = blevel #error checking
    update = 1

def reset(channel):
    global mlevel, update, blevel, reseter
    if reseter == 1:
        reseter = 0
    else :
        reseter = 1
        blevel = mlevel
        mlevel = 1
        update = 1

def select(channel):
    global timer, sub_menu, reseter
    if sub_menu == 1 :
        run = timer
        minute = 0
        second = 0
        hour = 0
        while minute <= run:
            if reseter == 1 :
                msg = "<<>>"
                show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT),scroll_delay=0.1)
                reseter = 0
                break
            msg = [minute,second]
            if minute >= run:
                while reseter != 1 :
                    msg = str(minute)
                    msg = str(msg).replace(" ","").replace('[','').replace(']','')
                    msg2 = ("!> " + msg + " <!")
                    with canvas(device) as draw:
                        text(draw, (1, 1), msg2, fill="white",font=proportional(TINY_FONT))
                    time.sleep(2)
                    sub_menu = 0
                    msg3 = str("")
                    with canvas(device) as draw:
                        text(draw, (1, 1), msg3, fill="white",font=proportional(TINY_FONT))
                    time.sleep(0.5)
                if reseter == 1 :
                    msg = "<<>>"
                    show_message(device, msg, fill="white", font=proportional(SINCLAIR_FONT),scroll_delay=0.1)
                    reseter = 0
                    break
            with canvas(device) as draw:
                msg = str(msg).replace(" ","").replace('[','').replace(']','')
                text(draw, (5, 1), msg, fill="white",font=proportional(TINY_FONT))
            time.sleep(1)
            second+=1
            if(second == 60):
                second = 0
                minute+=1
            if(minute == 60):
                minute = 0
                hour+=1;
    else :
        global  mlevel, update, blevel
        blevel = mlevel

        if mlevel == 2: select_level1()
        if mlevel == 3: select_level2()
        if mlevel == 4: select_level3()
        if mlevel == 5: select_level4()
        if mlevel == 6: select_level5()
        if mlevel == 7: select_level6()

        update = 1

GPIO.add_event_detect(17, GPIO.RISING, callback=up, bouncetime=200)
GPIO.add_event_detect(27, GPIO.RISING, callback=down, bouncetime=200)
GPIO.add_event_detect(24, GPIO.RISING, callback=reset, bouncetime=200)
GPIO.add_event_detect(23, GPIO.RISING, callback=select, bouncetime=200)
GPIO.add_event_detect(22, GPIO.RISING, callback=left, bouncetime=200)
GPIO.add_event_detect(18, GPIO.RISING, callback=right, bouncetime=200)

#loop to update menu on LCD
try :
    print ("  ###################")
    time.sleep (0.5)
    print ("  #  Pi             #", end="\r")
    time.sleep (0.5)
    print ("  #  PiCl           #", end="\r")
    time.sleep (0.2)
    print ("  #  PiClock        #", end="\r")
    time.sleep (0.2)
    print ("  #  PiClockM       #", end="\r")
    time.sleep (0.2)
    print ("  #  PiClockMat     #", end="\r")
    time.sleep (0.2)
    print ("  #  PiClockMatr    #", end="\r")
    time.sleep (0.2)
    print ("  #  PiClockMatrix  #")
    time.sleep (0.2)
    print ("  ###################")
    time.sleep (0.2)
    print ("  v0.10       by SMITH001")
    time.sleep (0.2)
    print("")
    print ("[ Ctrl + c ] == [ Exit ] ")
    while True:
        while update ==0:
            time.sleep (0.1)


        lcd.lcd_clear()

        if mlevel == 1: level1()
        if mlevel == 2: level2()
        if mlevel == 3: level3()
        if mlevel == 4: level4()
        if mlevel == 5: level5()
        if mlevel == 6: level6()
        if mlevel == 7: level7()

        update = 0

except KeyboardInterrupt:
    lcd.lcd_clear()
    sys.exit()
