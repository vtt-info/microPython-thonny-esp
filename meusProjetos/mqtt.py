#
# example ESP8266 or ESP32 Huzzah mqtt publish/subscribe with io.adafruit.com
# phil van allen
#
# thanks to https://github.com/MikeTeachman/micropython-adafruit-mqtt-esp8266/blob/master/mqtt-to-adafruit.py
#

import network
import time
import machine
from umqtt.simple import MQTTClient

pin = machine.Pin(27, machine.Pin.OUT) # LED on the board

def sub_cb(topic, msg):
    value = float(str(msg,'utf-8'))
    print("subscribed value = {}".format(value))
    if value > 4:
      pin.value(1)
    else:
      pin.value(0)

#
# connect the ESP to local wifi network
#
yourWifiSSID = "<Oficina>"
yourWifiPassword = "<1>"
sta_if = network.WLAN(network.STA_IF)
if not sta_if.isconnected():
  sta_if.active(True)
  sta_if.connect(yourWifiSSID, yourWifiPassword)
  while not sta_if.isconnected():
    pass
print("connected to WiFi")

#
# connect ESP to Adafruit IO using MQTT
#
myMqttClient = "esp32"  # substitua pelo seu próprio nome de cliente
adafruitUsername = "Edison_MB"  # pode ser encontrado em "Minha conta" em adafruit.com
adafruitAioKey = "aio_RGWC25yxMdF3F0HHFZEHnuDkgQNa"  #pode ser encontrado clicando em "VIEW AIO KEYS" ao visualizar um Adafruit IO Feed
adafruitFeed = adafruitUsername + "botao" # substitua "teste" pelo nome do seu feed
adafruitIoUrl = "io.adafruit.com"

c = MQTTClient(myMqttClient, adafruitIoUrl, 0, adafruitUsername, adafruitAioKey)
c.set_callback(sub_cb)
c.connect()
c.subscribe(bytes(adafruitFeed,'utf-8'))

for i in range(10):
  print(i)
  c.publish(adafruitFeed, str(i))
  time.sleep(2)
  c.check_msg()

c.disconnect()