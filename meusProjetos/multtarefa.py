#
# example ESP32 multitasking
# phil van allen
#
# thanks to https://youtu.be/iyoS9aSiDWg
#
import _thread as th
import time
from machine import Pin

blink1_running = True
blink2_running = True

led1 = Pin(26, Pin.OUT)
led2 = Pin(27, Pin.OUT)

def blink1():
     while blink1_running:
         led1.value(not led1.value())
         time.sleep(1)
     led1.value(1)

def blink2():
     while blink2_running:
         led2.value(not led2.value())
         time.sleep(0.1)
     led2.value(0)

print("Starting other tasks...")
th.start_new_thread(blink1,())
th.start_new_thread(blink2,())

# count = 0
# while True:
#   print("Doing stuff... " + str(count))
#   count += 1
#   if count >= 10:
#     break
#   time.sleep(1)
# 
# print("Ending threads...")
# blink1_running = False
# blink2_running = False