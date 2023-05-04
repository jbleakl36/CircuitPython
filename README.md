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


### Description & Code

We were taskes with using the tmp 36 and LCD screen to properally convey the change in temperature. Furthermore we were tasked to print
a message for if it's too hot and another message for if it's too cold. Learning goal: to fully understand how to weld the tempeture sensor.

```python
import board
import analogio
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
TMP36_PIN = board.A1  # Analog input connected to TMP36 output.
i2c = board.I2C()

Function to simplify the math of reading the temperature.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)
def tmp36_temperature_C(analogin):
    millivolts = analogin.value * (analogin.reference_voltage * 1000 / 65535)
    return (millivolts - 500) / 10


 Create  analog input.
tmp36 = analogio.AnalogIn(board.A1)

Loop forever.
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
```


### Evidence
https://user-images.githubusercontent.com/112979207/225112713-0ce9ac49-74fd-44bd-8d0d-4298f7ec97ba.mp4

### Wiring
![Yo](https://user-images.githubusercontent.com/112979207/225115168-0909b9d9-194b-4c3a-971d-4f98e474b818.png)


### Reflection
Initially hard but evetually understood the way an LCD screen worked again. I learned that even if things are going smoothly that there will most likely be set backs and that is frustrating but it is part of the challenge of coding. My t 36 was in the 19's temprature wise but besides that
there wasn't much issue.
### Rotary encoder

### Description and code
We were tasked with using a rotary encoder, lcd screen, and 3 leds to create a menu based traffic control. We had to utilize the 
three pins of the rotary encoder to have it working properly. Learning goal: To understand how to use the rotary encoder and to
learn four new programming concepts those being Constants, String objects, Arrays, and the switch case statement.

```python
Rotary Encodare light thingksf;ja

import time

import rotaryio

import board

from lcd.lcd import LCD

from lcd.i2c_pcf8574_interface import I2CPCF8574Interface

from digitalio import DigitalInOut, Direction, Pull



encoder = rotaryio.IncrementalEncoder(board.D3, board.D2)

last_position = 0

btn = DigitalInOut(board.D1)

btn.direction = Direction.INPUT

btn.pull = Pull.UP

state = 0

Buttonyep = 1



i2c = board.I2C()

lcd = LCD(I2CPCF8574Interface(i2c, 0x27), num_rows=2, num_cols=16)



ledGreen = DigitalInOut(board.D8)

ledYellow = DigitalInOut(board.D9)

ledRed = DigitalInOut(board.D10)

ledGreen.direction = Direction.OUTPUT

ledYellow.direction = Direction.OUTPUT

ledRed.direction = Direction.OUTPUT



while True:

    position = encoder.position

    if position != last_position:

        if position > last_position:

            state = state + 1

        elif position < last_position:

            state = state - 1

        if state > 2:

            state = 2

        if state < 0:

            state = 0

        print(state)

        if state == 0: 

            lcd.set_cursor_pos(0, 0)

            lcd.print("GOOOOO")

        elif state == 1:

            lcd.set_cursor_pos(0, 0)

            lcd.print("yellow")

        elif state == 2:

            lcd.set_cursor_pos(0, 0)

            lcd.print("STOPPP")

    if btn.value == 0 and Buttonyep == 1:

        print("buttion")

        if state == 0: 

                ledGreen.value = True

                ledRed.value = False

                ledYellow.value = False

        elif state == 1:

                ledYellow.value = True

                ledRed.value = False

                ledGreen.value = False

        elif state == 2:

                ledRed.value = True

                ledGreen.value = False

                ledYellow.value = False

        Buttonyep = 0

    if btn.value == 1:

        time.sleep(.1)

        Buttonyep = 1

    last_position = position
```

### Evidence
![226446966-8a585aef-7c21-480a-8ca3-219ae95f4cef](https://user-images.githubusercontent.com/112979207/226720029-20b73fc3-1464-41d9-80bd-444d2c4761ca.gif)

### Reflection 
It was initially tricky, there were so many concepts indroduced at once I didn't even know where to begin. But as I began to go over the designated slideshow it became less intimidating. The major problems I had were the fact that Github was down and the fact that I didn't have rotaryio imported for some reason.

### Photointerupters

### Descrtiption and code
We were tasked with using a photointerupter to keep track of how many times it has been interrupted. Furthermore we needed to make sure it was wired properly
as if we didn't we would fry the photointerupter. Learning goal: To properly understand how the photointerupter works and to learn how to create a coding sequence 
without using the sleep command but instead using the time.monocromatic command instead.

```python
import time
import digitalio
import board

photoI = digitalio.DigitalInOut(board.D7)
photoI.direction = digitalio.Direction.INPUT
photoI.pull = digitalio.Pull.UP

last_photoI = True
last_update = -4

photoICrosses = 0

while True:
    if time.monotonic()-last_update > 4:
        print(f"The number of crosses is {photoICrosses}")
        last_update = time.monotonic()
    
    if last_photoI != photoI.value and not photoI.value:
        photoICrosses += 1
    last_photoI = photoI.value
```

### Evidence

![226713736-399d0f22-aff7-4dd4-8ebb-a26b9d3674bc](https://user-images.githubusercontent.com/112979207/228343671-c46b8f40-732a-407d-82b8-e0a1ecd68265.gif)

### Wiring 
![68747470733a2f2f726976717565732e6769746875622e696f2f646f63732f70686f746f696e74636972637569742e706e67](https://user-images.githubusercontent.com/112979207/228343647-98e76c17-ba22-464a-a1ec-a0ea43d0b802.png)

### Reflection
I am thankful that the wiring was broken down for us because if not, I would have totally fryed a photointerupter. Besides the wiring learning the time.monocromatic was a bit tricky but after some research I eventually learned it's ways. It was exciting seeing it work for the first time as other assingments have taken much longer than the time I took to finish this one.
