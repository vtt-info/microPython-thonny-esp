#
# example ESP32 multitasking
# phil van allen
#
# thanks to https://youtu.be/iyoS9aSiDWg
#
import _thread as th
import time
from machine import Pin

led1 = Pin(26, Pin.OUT)
led2 = Pin(27, Pin.OUT)

def blink1():
     while 1 :
         led1.value(not led1.value())
         time.sleep(1)
     led1.value(1)

def blink2():
     while 1 :
         led2.value(not led2.value())
         time.sleep(0.1)
     led2.value(0)

print("Starting other tasks...")
th.start_new_thread(blink1,())
th.start_new_thread(blink2,())

