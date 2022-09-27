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
![sssservoo wiring](https://user-images.githubusercontent.com/112979207/192616324-de282856-b597-4414-8e24-c83be13c3695.png)

### Reflection

I had a few troubles, first off uploading the adafruit_motor was a challange. Getting the hang of the code and how to implement the "for angle in range" feature was really hard. But in the end it worked out for me which is all I could ask for.

## CircuitPython_LCD

### Description & Code

```python
Code goes here

```

### Evidence

Pictures / Gifs of your work should go here.  You need to communicate what your thing does.

### Wiring

### Reflection





## CircuitPython_Distance sensor

### Description & Code

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

### Reflection
This was the hardest assingment I have done yet. Learning how to properally use the map_range was insanely hard but once I figured it out I really got the hang of it. It was a challange to get a clear demonstration but I was able to do it in the end.
