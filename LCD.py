#type: ignore
import board
import time
from lcd.lcd import LCD
from lcd.i2c_pcf8574_interface import I2CPCF8574Interface
from digitalio import DigitalInOut, Direction, Pull
# get and i2c object
i2c = board.I2C()

# some LCDs are 0x3f... some are 0x27.
lcd = LCD(I2CPCF8574Interface(i2c, 0x3f), num_rows=2, num_cols=16)

buttonpress=0
btn1 = DigitalInOut(board.D2)
btn2 = DigitalInOut(board.D3)
btn1.direction = Direction.INPUT
btn1.pull = Pull.UP
btn2.direction = Direction.INPUT
btn2.pull = Pull.UP
cur_state = True
prev_state = True



while True:
 
    curr_state= btn2.value
    
    
    if cur_state != prev_state:
        if not cur_state:
            lcd.print("BTN1 is down")
            cur_state= False
            prev_state= False
          
        else:
            lcd.print("BTN1 is up")
            buttonpress = buttonpress + 1
    prev_state = cur_state
    time.sleep(.05)
    
    