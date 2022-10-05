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