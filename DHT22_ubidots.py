from ubidots import ApiClient
import random
import time
import sys
import Adafruit_DHT

#Set the type of sensor and the pin for sensor
sensor = Adafruit_DHT.DHT22
pin = 4

# Create an ApiClient object

api = ApiClient(token='xxxxxxxxxxxxxxxxxxxxxxxxxxxxx')

# Get a Ubidots Variable

try:
    variable1 = api.get_variable("xxxxxxxxxxxxxxxxxxxxxxxx")
    variable2 = api.get_variable("xxxxxxxxxxxxxxxxxxxxxxxx")

except ValueError:
    print"It is not possible to obtain the variable"

while(1):
    try:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        variable1.save_value({'value': humidity})
        variable2.save_value({'value': temperature})
	print "Value sent"
        time.sleep(120)
    except ValueError:
        print "Value not sent"

