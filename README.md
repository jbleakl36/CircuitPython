# CircuitPython
This repository will actually serve as a aid to help you get started with your own template.  You should copy the raw form of this readme into your own, and use this template to write your own.  If you want to draw inspiration from other classmates, feel free to check [this directory of all students!](https://github.com/chssigma/Class_Accounts).
## Table of Contents
* [Table of Contents](#TableOfContents)
* [Hello_CircuitPython](#Hello_CircuitPython)
* [CircuitPython_Servo](#CircuitPython_Servo)
* [CircuitPython_LCD](#CircuitPython_LCD)
* [NextAssignmentGoesHere](#NextAssignment)
---

## Hello_CircuitPython

### Description & Code
Description goes here

Here's how you make code look like code:

```python
Code goes here

```


### Evidence


![spinningMetro_Optimized](https://user-images.githubusercontent.com/54641488/192549584-18285130-2e3b-4631-8005-0792c2942f73.gif)


And here is how you should give image credit to someone, if you use their work:

Image credit goes to [Rick A](https://www.youtube.com/watch?v=dQw4w9WgXcQ&scrlybrkr=8931d0bc)



### Wiring
Make an account with your google ID at [tinkercad.com](https://www.tinkercad.com/learn/circuits), and use "TinkerCad Circuits to make a wiring diagram."  It's really easy!  
Then post an image here.   [here's a quick tutorial for all markdown code, like making links](https://guides.github.com/features/mastering-markdown/)

### Reflection
What went wrong / was challenging, how'd you figure it out, and what did you learn from that experience?  Your ultimate goal for the reflection is to pass on knowledge that will make this assignment better or easier for the next person.




## CircuitPython_Servo

### Description & Code

We were assinged to get a 180° micro servo to slowly sweep back and forth between 0 and 180°.   
```python
# SPDX-FileCopyrightText: 2018 Kattni Rembor for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""CircuitPython Essentials Servo standard servo example"""
import time
import board
import pwmio
from adafruit_motor import servo
# create a PWMOut object on Pin A2.
pwm = pwmio.PWMOut(board.D3, duty_cycle=2 ** 15, frequency=50)

# Create a servo object, my_servo.
my_servo = servo.Servo(pwm)

while True:
    for angle in range(0, 180, 100):  # 0 - 180 degrees, 100 degrees at a time.
        my_servo.angle = angle
        time.sleep(2)
        print("Go forth") # added for the requirement
    for angle in range(180, 0, -100): # 180 - 0 degrees, 100 degrees at a time.
        my_servo.angle = angle
        time.sleep(2)
        print("Steer back") #Same here

```

### Evidence

https://cvilleschools.instructure.com/courses/37129/assignments/493862/submissions/4669

### Wiring
![Servo!!!!!](https://user-images.githubusercontent.com/112979207/192621243-145f76de-b0d5-4bc2-b9d3-eab04ff97999.png)


### Reflection

I had a few troubles, first off uploading the adafruit_motor was a challange. Getting the hang of the code and how to implement the "for angle in range" feature was really hard. But in the end it worked out for me which is all I could ask for.

## CircuitPython_LCD

### Description & Code

We were assinged to used two buttons and have thier inputs be shown on the LCD screen. One button adds or subtracts one, then the other determines wheither it is a postive or a negetive.
```python

#Elias Garcia
#When a button is presses it increses or decreases the count based on the position of a switch
#Code from Grant Gastinger
 
import board
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
import time
from digitalio import DigitalInOut, Direction, Pull

# get and i2c object
i2c = board.I2C()
btn = DigitalInOut(board.D2)
btn.direction = Direction.INPUT
btn.pull = Pull.UP
clickCount = 0

btn2 = DigitalInOut(board.D3)
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
# some LCDs are 0x3f... some are 0x27...
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

lcd.print("elias")
print("son, i am disapoint.")
while True:
    if not btn2.value:
        if not btn.value:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Click Count:")
            lcd.set_cursor_pos(0,13)
            clickCount = clickCount + 1
            lcd.print(str(clickCount))
        else:
            pass
    else:
        if not btn.value:
            lcd.clear()
            lcd.set_cursor_pos(0, 0)
            lcd.print("Click Count:")
            lcd.set_cursor_pos(0,13)
            clickCount = clickCount - 1
            lcd.print(str(clickCount))
        else:
            pass
    print("btn1",btn.value,"   btn2",btn2.value)

    time.sleep(0.1) # sleep for debounce
```

### Evidence
Preview attachment IMG_0880.MOV

IMG_0880.MOV
3.5 MB

### Wiring
![Real LCD!!!!!](https://user-images.githubusercontent.com/112979207/193122912-42deb280-2e60-49e8-9e4a-d782b3baa57a.png)


### Reflection

In all this assignment was brutally hard. My LCD short curcuited and it took me weeks to finish. Adivce: Make sure your wiring is good before you go or else your computer will put you on safe mode.



## CircuitPython_Distance sensor

### Description & Code

We were assinged to use the distance sensor to successfully alter the color of an led light depending on what distance it read.
```python
#type: ignore
import simpleio
import time
import board
import adafruit_hcsr04
import neopixel
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D4)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.1
red =0
blue =0
green =0
 
while True:

    try:
        print((sonar.distance, red, green, blue))
        
        if sonar.distance < 5:
            red= simpleio.map_range(sonar.distance, 0, 5, 255, 0)
            blue= simpleio.map_range(sonar.distance, 0, 5, 0, 255)
            green= 0
            dot.fill((red, 0, blue))
        elif sonar.distance < 20 and sonar.distance> 5:
             red= 0
             blue= simpleio.map_range(sonar.distance, 5, 20, 255, 0)
             green= simpleio.map_range(sonar.distance, 5, 20, 0, 255)
             dot.fill((0, green, blue))
        else:
             red=0
             green= simpleio.map_range(sonar.distance, 20, 400, 255, 0)
             blue= simpleio.map_range(sonar.distance, 20, 100, 0, 25)
             dot.fill((0, green, blue))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)

```

### Evidence
https://cvilleschools.instructure.com/courses/37129/assignments/493861/submissions/4669
### Wiring
![sssservoo wiring](https://user-images.githubusercontent.com/112979207/192616324-de282856-b597-4414-8e24-c83be13c3695.png)
### Reflection
This was the hardest assingment I have done yet. Learning how to properally use the map_range was insanely hard but once I figured it out I really got the hang of it. It was a challange to get a clear demonstration but I was able to do it in the end.

### Motor Control

### Description & Code
We were tasked with wiring a Dc motor and using a potentiometer to control it's rate

```python
import time
import board
from analogio import AnalogIn,AnalogOut
from digitalio import DigitalInOut, Direction, Pull
import simpleio
from adafruit_motor import motor 

motorpin = AnalogOut(board.A1)
potentiometer = AnalogIn(board.A0)  # potentiometer connected to A1, power & ground

while True:

    print((int(simpleio.map_range(potentiometer.value,0,65535,0,255))))     
    time.sleep(0.25) 
    motorpin.value = potentiometer.value
```

### Evidence


https://user-images.githubusercontent.com/112979207/199818663-7a93eebd-2407-40db-b45e-18ec1f43f4ca.MOV

### Wiring 
![Yay](https://user-images.githubusercontent.com/112979207/199820945-bab03dd0-8159-46b3-ae11-1b1a71e2f276.png)


### Reflection
This assingment was frustrating. My computer didn't let me use my COM making the serial monitor useless 
to me. My DC motor was very strong and gave me trouble when I had to evaluate the speed. Overall
it wasn't fun (especially the coding) but in the end, I have finsihed and I don't have to worry about
this anymore (I hope I am not acidentally foreshadowing)

### Temp

import board
import analogio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
TMP36_PIN = board.A1  # Analog input connected to TMP36 output.
i2c = board.I2C()

# Function to simplify the math of reading the temperature.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10


# Create  analog input.
tmp36 = analogio.AnalogIn(board.A1)

# Loop forever.
while True:
    # Read the temperature in Celsius.
    temp_C = tmp36_temperature_C(tmp36)
    # Convert to Fahrenheit.
    temp_F = (temp_C * 9/5) + 32
    # Print out the value and delay a second before looping again.
    lcd.set_cursor_pos(0, 0)
    lcd.print("Temp: {}".format(temp_F))
    time.sleep(.5)
    lcd.set_cursor_pos(0,1)
    if temp_C >= 30:
        lcd.set_cursor_pos(0, 13)
        lcd.print("Heat")
    else:
        lcd.set_cursor_pos(0, 12)
        lcd.print("Cold")
    time.sleep(.5)
