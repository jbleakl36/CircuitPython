#type: ignore
import simpleio
import time
import board
import adafruit_hcsr04
import neopixel
sonar = adafruit_hcsr04.HCSR04(trigger_pin=board.D5, echo_pin=board.D4)
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 
red =0
blue =0
green =0
 
while True:

    try:
        print((sonar.distance, red, green, blue))
        
        if sonar.distance < 5:
            red= simpleio.map_range(sonar.distance, 5, 20, 0, 255)
            blue= 0
            green= 0
            dot.fill((red, 0, 0))
        elif sonar.distance < 20 and sonar.distance> 5:
             red= 0
             blue= simpleio.map_range(sonar.distance, 5, 20, 0, 255)
             green= 0
             dot.fill((0, 0, blue))
        else:
             red=0
             green= simpleio.map_range(sonar.distance, 5, 20, 0, 255)
             blue= 0
             dot.fill((0, green, 0))
    except RuntimeError:
        print("Retrying!")
    time.sleep(0.1)
    