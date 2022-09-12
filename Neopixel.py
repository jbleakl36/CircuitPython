import board
import neopixel
import time
dot = neopixel.NeoPixel(board.NEOPIXEL, 1)
dot.brightness = 0.5 

print("Make it red!")

while True:
    dot.fill((249, 0, 0))
    time.sleep(1)
    dot.fill((255, 128, 0))
    time.sleep(1)
    dot.fill((255, 247, 0))
    time.sleep(1)
    dot.fill((0, 222, 7))
    time.sleep(1)
    dot.fill((0, 108, 249))
    time.sleep(1)
    dot.fill((191, 0, 249))