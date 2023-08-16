# PiClockMatrix

[![Version](https://img.shields.io/badge/Version-0.10-blue.svg)](https://github.com/Superjulien/Piclockmatrix) [![License](https://img.shields.io/badge/License-MIT-blue.svg)](https://choosealicense.com/licenses/mit/) [![Python](https://img.shields.io/badge/Python_3-14354C?&logo=python&logoColor=white.svg)](https://www.python.org/)

This Python script provides a versatile clock application for a Raspberry Pi, utilizing an LCD display, LED matrix, and GPIO buttons for interaction. The script offers multiple menu levels, each providing distinct functionalities and information displays.

## Main Features

### Hardware Setup:
- Utilizes an LCD display for menu and information display.
- Utilizes an LED matrix for visual notifications.
- Utilizes GPIO buttons (UP, DOWN, LEFT, RIGHT, SELECT, RESET) for user interaction.

### Functionality:
- Displays various menu levels on the LCD screen.
- Navigates through menu options using UP and DOWN buttons.
- Executes selected actions using the SELECT button.
- Resets the menu or timer using the RESET button.
- Provides options such as displaying the IP address, weather information, countdown, timer, and more.

### Menu Levels and Actions:
- Defines multiple menu levels (`level1` to `level7`) with associated actions.
- Provides functions for each menu level to display relevant information.

### Button Callbacks:
- Maps button presses (UP, DOWN, SELECT, etc.) to corresponding callback functions.
- Callbacks handle navigation, selection, and resetting actions.

### Main Loop:
- Enters a continuous main loop that updates the LCD display based on the current menu level.
- Responds to button presses and triggers appropriate actions.

### Customization and Adaptation: 
- Requires customization of specific variables (e.g., `lang`, `city`, `key`) to match your use case.
- Can be adapted to different hardware setups or requirements.

**Note**: This script serves as a foundational Raspberry Pi clock application and may need further development and customization to align with your project goals. It demonstrates how to create a menu-driven interface with diverse features using an LCD display, LED matrix, and GPIO buttons.

Before using this script, ensure you understand the interactions between components and tailor variables and functionalities to your project's needs. Adaptation and customization are essential for successful implementation.

## Menu Options:

#### Info&Date:
- Displays system hostname, IP address.
- Presents the current date with day, month, and year.

#### Weather:
- Fetches real-time weather information from OpenWeather using the configured city and API key.
- Displays the current weather conditions, including temperature, humidity, and weather description.
- Provides weather forecasts for the next 24 hours, with temperature and weather condition changes.

#### Countdown:
- Allows users to set a countdown timer for a specific duration using LEFT and RIGHT buttons.
- Displays the remaining time on the LCD screen in a user-friendly format (HH:MM:SS).

#### Watch:
- Displays the current time in hours, minutes, and seconds.
- Offers continuous updates to keep users informed of the accurate time.

#### Stopwatch:
- Provides a running stopwatch that counts elapsed time in hours, minutes, and seconds.
- Offers a START/STOP functionality using the SELECT button for precise time tracking.
- Enables users to measure elapsed time for various purposes.

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

# Installation Steps
## Hardware Setup :
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
|    GND      |    GND       |
|    VCC      |    5V        |
|    SDA      |    #2 SDA    |
|    SCL      |    #3 SCL    |

### Schema

Consult the [Schema](https://github.com/Superjulien/piclockmatrix/blob/main/schema/Untitled.png) for reference.

 ![Schema_connecteur](https://github.com/Superjulien/piclockmatrix/blob/main/schema/Untitled.png) 

## Software Setup:

Follow these steps to set up the necessary software components for PiClockMatrix:

1. Update and upgrade the package list:
```bash
sudo apt update && sudo apt upgrade -y
```

2. Install required packages:
```bash
sudo apt install git python3 python3-smbus python3-dev i2c-tools build-essential python3-pip libfreetype6-dev libjpeg-dev libopenjp2-7 libtiff5 
```

3. Configure `config.txt`:
Edit the configuration file using the nano text editor:
```bash
sudo nano /boot/config.txt
```
Add the following lines at the bottom of the file:
```
dtparam=i2c_arm=on
dtparam=spi=on
```
Save and exit by pressing CTRL-X, then Y, then RETURN.

4. Configure `modules`:
```bash
sudo nano /etc/modules
```
Add the following lines at the end of the file:
```
i2c-bcm2708  
i2c-dev
```
Save and exit by pressing CTRL-X, then Y, then RETURN.

5. Reboot the Raspberry Pi:
```bash
sudo reboot
```

6. Install required Python libraries:
```bash
sudo pip3 install luma.led_matrix pyowm RPi.GPIO 
```

7. Clone the PiClockMatrix repository:
```bash
git clone https://github.com/Superjulien/piclockmatrix.git
```

8. Edit `piclockmatrix.py`:
Navigate to the `piclockmatrix` directory and edit the `piclockmatrix.py` file to customize the weather settings:
```bash
cd piclockmatrix
nano piclockmatrix.py
```
Change the following lines to match your preferences:
```python
# Setting weather:
lang = 'EN'
city = 'City,EN'
key = 'api-key'
```
Save the changes and exit the editor.

## Usage:

Run the PiClockMatrix script with the following command:
```bash
sudo python3 piclockmatrix.py
```
The script includes exception handling to ensure a graceful exit when the user interrupts the program (Ctrl+C).

### Using Buttons in the Script:

The PiClockMatrix script utilizes GPIO buttons (UP, DOWN, LEFT, RIGHT, SELECT, RESET) to interact with application. Here's how to use these buttons to navigate through menus and perform actions:

1. **Navigation Buttons (UP and DOWN):**

   - The "UP" button is used to navigate to the previous menu or move the selection upward.
   - The "DOWN" button is used to navigate to the next menu or move the selection downward.

2. **Selection Button (SELECT):**

   - The "SELECT" button is used to execute the action associated with the selected option in the menu.

3. **Reset Button (RESET):**

   - The "RESET" button is used to reset the menu or timer, depending on the context.

4. **Scroll Buttons (LEFT and RIGHT):**

   - In certain menus, the "LEFT" and "RIGHT" buttons can be used to move the selection horizontally, for example, to adjust the countdown.

5. **Center Button (MID):**

   - The "MID" button can be used to perform specific actions in different menus, for example this action could involve displaying specific information, triggering a timer, showing weather data ...

#### Example of Use:

1. Upon starting the application, you'll see a main screen with menu options.

2. Use the "UP" and "DOWN" buttons to select the desired menu.

3. Press the "SELECT" button to confirm your selection and access the submenu or execute the associated action.

4. In certain menus, use the "LEFT" and "RIGHT" buttons to adjust settings, such as timer adjustment.

5. Press the "MID" button to perform special actions, such as starting or stopping a timer.

6. To reset the menu or timer, press the "RESET" button.

#### Countdown:

1. **Activating the Countdown**: When you access the level 4 menu, you have the option to select a time for the countdown. The "Left" and "Right" buttons adjust the countdown value.

2. **Starting the Countdown**: Once you've selected the desired time, press the "Select" button to start the countdown. The script will then enter a loop that displays the remaining time on the LCD screen.

3. **Updating the Countdown**: The script updates the countdown display every second. The remaining time is displayed in minutes and seconds. When the time reaches zero, the countdown stops.

4. **End of Countdown**: Once the countdown is complete, you can press any button to return to the main menu.

5. **Countdown Interruption**: At any point during the countdown, if you press the "Reset" button, the countdown will be interrupted, and you will be taken back to the main menu.

#### Stopwatch:

1. **Activating the Stopwatch**: When you access the level 7 menu, you have the option to start the stopwatch. Press the "Select" button to begin timing.

2. **Measuring Time**: The script starts measuring time once you've started the stopwatch. The display will continuously update to show the elapsed time in hours, minutes, and seconds.

3. **Pause and Resume**: You can pause the stopwatch at any point by pressing the "Select" button again. Press "Select" again to resume timing.

## Celsius to Fahrenheit Conversion:

To convert temperature from Celsius to Fahrenheit in the script, make the following modifications:

In the select_level2 function, change the line
```
temp_dict_celsius = weather.temperature('celsius')
```
to
```
temp_dict_fahrenheit = weather.temperature('fahrenheit')
```
change the line
```
temp_dict_celsius2 = weather.temperature('celsius')
```
to
```
temp_dict_fahrenheit2 = weather.temperature('fahrenheit')
```
change the line
```
meteo = str(str(temp_dict_celsius['temp'])+"C "+str(status).replace('é','e').replace('è','e')+" "+str(temp_dict_celsius['feels_like'])+"C +"+str(temp_dict_celsius['temp_max'])+"C -"+str(temp_dict_celsius['temp_min'])+"C Hum:"+ str(hum)+"% Wind:"+str(wind_dict_in_meters_per_sec['speed']) +"m/s "+"Sun:"+str(sunrise_date.strftime('%H:%M:%S'))+" - "+str(sunrset_date.strftime('%H:%M:%S'))+" || Tomorrow at "+str(h)+"h : "+str(temp_dict_celsius2['temp'])+"C "+str(status2).replace('é','e').replace('è','e')+" "+str(temp_dict_celsius2['feels_like'])+"C")
```
to
```
meteo = str(str(temp_dict_fahrenheit['temp']) + "F " + str(status).replace('é', 'e').replace('è', 'e') + " " + str(temp_dict_fahrenheit['feels_like']) + "F +" + str(temp_dict_fahrenheit['temp_max']) + "F -" + str(temp_dict_fahrenheit['temp_min']) + "F Hum:" + str(hum) + "% Wind:" + str(wind_dict_in_meters_per_sec['speed']) + "m/s " + "Sun:" + str(sunrise_date.strftime('%H:%M:%S')) + " - " + str(sunrset_date.strftime('%H:%M:%S')) + " || Tomorrow at " + str(h) + "h : " + str(temp_dict_fahrenheit2['temp']) + "F " + str(status2).replace('é', 'e').replace('è', 'e') + " " + str(temp_dict_fahrenheit2['feels_like']) + "F")
```

## Customizable Functions:

PiClockMatrix provides several customizable functions that allow you to tailor the behavior and features of the clock application to your specific needs. Here are some of the key customizable functions:

1. **Weather Data Retrieval:**
   - You can customize the city and language settings to get weather information for your desired location and language.

2. **Displaying Weather Information:**
   - You can modify the formatting, layout, and additional details displayed about the weather.

3. **Countdown Timer:**
   - You can customize the display and behavior of the countdown.

4. **Custom Menus and Actions:**
   - You can modify these functions to create new menu options or change the behavior of existing menus.

5. **Button Callbacks:**
   - You can customize these functions to define different actions or behaviors when specific buttons are pressed.

6. **Additional Customization:**
   - PiClockMatrix uses various variables to control settings and behavior.
   - You can adjust these variables to customize aspects such as language, date/time formats, and display configurations.

7. **Interaction with External APIs:**
   - PiClockMatrix interacts with the OpenWeather API using the PyOWM library to fetch weather data.
   - You can explore the PyOWM documentation to customize weather data retrieval or incorporate other APIs.

8. **LCD Display and LED Matrix:**
   - The luma.led_matrix library controls the LCD display and LED matrix.
   - You can modify settings and configurations to adjust the appearance and behavior of the display.

Remember that customization involves understanding the script's structure, function interactions, and external library usage. Be cautious when making changes, and consider testing each modification to ensure the desired functionality is achieved.

Feel free to explore, experiment, and customize PiClockMatrix to create a unique clock application tailored to your needs.

## Warnings and Considerations:

- The use of hardware components requires a proper understanding of GPIO pins and hardware interactions.
- Make sure to correctly connect the hardware components according to the provided diagram and manufacturer's instructions.
- This script may require modifications and adjustments to fit different hardware configurations or address specific needs.
- Ensure you understand the code and script functionalities before running it on your Raspberry Pi.
- Customizing the script requires basic knowledge of Python programming.
- Sensitive variables such as the weather API key must be handled with caution and should not be shared publicly.
- This script is provided "as is" and may require updates or further adjustments based on changes in libraries, APIs, and your project's requirements.

## Upcoming Features

- Implementation of the `def level4():`.
- Enhanced stability and performance.
- Bug fixes.

## Documentation

- [HW-109 lcd MAX7219](https://datasheets.maximintegrated.com/en/ds/MAX7219-MAX7221.pdf)
- [Five Direction button](https://electropeak.com/learn/interfacing-5-direction-joystick-button-module-with-arduino/)
- [1602 A LCD 5v](https://www.gotronic.fr/pj2-sbc-lcd16x2-fr-1441.pdf)
- [Python3](https://www.python.org/doc/)
- [luma.led_matrix](https://github.com/rm-hull/luma.led_matrix)
- [RPi_I2C_driver](https://www.recantha.co.uk/blog/?p=4849)
- [OpenWeather](https://openweathermap.org/)
- [PyOWM](https://pyowm.readthedocs.io/en/latest/)

## Sponsoring

This software is provided to you free of charge, with the hope that if you find it valuable, you'll consider making a donation to a charitable organization of your choice :

- SPA (Society for the Protection of Animals): The SPA is one of the oldest and most recognized organizations in France for the protection of domestic animals. It provides shelters, veterinary care, and works towards responsible adoption.

  [![SPA](https://img.shields.io/badge/Sponsoring-SPA-red.svg)](https://www.la-spa.fr/)

- French Popular Aid: This organization aims to fight against poverty and exclusion by providing food aid, clothing, and organizing recreational activities for disadvantaged individuals.

  [![SPF](https://img.shields.io/badge/Sponsoring-Secours%20Populaire%20Français-red.svg)](https://www.secourspopulaire.fr)

- Doctors Without Borders (MSF): MSF provides emergency medical assistance to populations in danger around the world, particularly in conflict zones and humanitarian crises.

  [![MSF](https://img.shields.io/badge/Sponsoring-Médecins%20Sans%20Frontières-red.svg)](https://www.msf.fr)

- Restaurants of the Heart : Restaurants of the Heart provides meals, emergency accommodation, and social services to the underprivileged.

  [![RDC](https://img.shields.io/badge/Sponsoring-Restaurants%20du%20Cœur-red.svg)](https://www.restosducoeur.org)

- French Red Cross: The Red Cross offers humanitarian aid, emergency relief, first aid training, as well as social and medical activities for vulnerable individuals.

   [![CRF](https://img.shields.io/badge/Sponsoring-Croix%20Rouge%20Française-red.svg)](https://www.croix-rouge.fr)

Every small gesture matters and contributes to making a real difference.

## Support
For support email : 

[![Gmail: superjulien](https://img.shields.io/badge/Gmail-Contact%20Me-purple.svg)](mailto:contact.superjulien@gmail.com) [![Tutanota: superjulien](https://img.shields.io/badge/Tutanota-Contact%20Me-green.svg)](mailto:contacts.superjulien@tutanota.com)

## License

PiClockMatrix is open-source software released under the [MIT License](https://choosealicense.com/licenses/mit/). You are free to use, modify, and distribute the software as per the terms of the license.
