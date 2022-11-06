# PiClockMatrix

Pyhon script for raspberry pi with a pcb joystick, LED matrix and lcd screen which gives the time, weather, date, countdown ects .... 

### Version
Version 0.10 - beta.

## Documentation

- [HW-109 lcd MAX7219](https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf)
- [Five Direction button](https://electropeak.com/learn/interfacing-5-direction-joystick-button-module-with-arduino/)
- [1602 A LCD 5v](https://www.gotronic.fr/pj2-sbc-lcd16x2-fr-1441.pdf)
- [Python3](https://www.python.org/doc/)
- [luma.led_matrix](https://github.com/rm-hull/luma.led_matrix)
- [RPi_I2C_driver](https://www.recantha.co.uk/blog/?p=4849)
- [OpenWeather](https://openweathermap.org/)
- [PyOWM](https://pyowm.readthedocs.io/en/latest/)

# Required
## Hardware :
- Raspberry Pi Model B Plus Rev 1.2 (x1)
- HW-109 lcd MAX7219 (x3)
- Five Direction button module (x1)
- 1602 A LCD 5v (x1)
## Software :
- Raspberry Pi OS lite v10 (buster)
- python 3
- OpenWeather account
- pyowm
- python3-smbus 
- python3-dev 
- i2c-tools
- build-essential 
- python3-pip 
- libfreetype6-dev 
- libjpeg-dev 
- libopenjp2-7 
- libtiff5
- RPi.GPIO 

# Installation
## Hardware :
### HW-109 lcd MAX7219
|  MAX7219  | Raspberry pi |
| --------- | ------------ |
|   VCC     |   5V         |
|   GND     |   GND        |
|   DIN     |   #10 MOSI   |
|   CS      |   #8 CE0     |
|   CLK     |   #11 SCLK   |
### Five Direction button module
| Five Direction  | Raspberry pi |
| --------------- | ------------ |
|     COM         |      GND     |
|     UP          |      #17     |
|     DWN         |      #27     |
|     LFT         |      #22     |
|     RHT         |      #18     |
|     MID         |      #23     |
|     SET         |      X       |
|     RST         |      #24     |
### 1602 A LCD 5v
| 1602 A LCD  | Raspberry pi |
| ----------- | ------------ |
|    GND      |    GND   |
|    VCC      |    5V   |
|    SDA      |    #2 SDA   |
|    SCL      |    #3 SCL   |
### Schema
 ![Schema_connecteur](https://github.com/Superjulien/piclockmatrix/blob/main/schema/Untitled.png) 


## Software :
```
sudo apt update && sudo apt upgrade -y
sudo apt install git python3 python3-smbus python3-dev i2c-tools build-essential python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5 
sudo nano /boot/config.txt
```
Add the following line at the bottom :
```
dtparam=i2c_arm=on
dtparam=spi=on
```
Use CTRL-X, then Y, then RETURN to save the file and exit. 

Open file modules.
```
sudo nano /etc/modules
```
Copy at the end :
```
i2c-bcm2708  
i2c-dev
```
Use CTRL-X, then Y, then RETURN to save the file and exit. 

Reboot using the following :
```
sudo reboot
```
```
sudo pip3 install luma.led_matrix pyowm RPi.GPIO 
git clone https://github.com/Superjulien/piclockmatrix.git
```
Edit piclockmatrix.py , change setting weather :
```
#Setting weather :
lang = 'EN'
city = 'City,EN'
key = 'api-key'
``` 

## Usage

```
sudo python3 piclockmatrix.py
```

### LCD selection
- Menu Selection Up / Down on joystick 
- Press MID for selection
- Press RST for all reset
- Countdown : Selection time with joystick (lft/rht)
### Menu list 
|  Menu     |   report           |
| --------- | -------------------|
| Info&Date | Write info & date  |
| Weather   | Write weather info |
| *******   | Nothing            |
| Countdown | Write countdown    |
| Watch     | Write clock        |                                        
| Stopwatch | Write stopwatch    |
### Examples :
```
  ###################
  #  PiClockMatrix  #
  ###################
  v0.10       by SMITH001

[ Ctrl + c ] == [ Exit ] 

```
## Features

- More stable
- Bug correction

## Support

For support, email [Gmail: superjulien](mailto:contact.superjulien@gmail.com) | [Tutanota: superjulien](mailto:contacts.superjulien@tutanota.com).

## License

[MIT](https://choosealicense.com/licenses/mit/)
