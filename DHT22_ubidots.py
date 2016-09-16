from ubidots import ApiClient
import random
import time
import sys
import Adafruit_DHT

#Set the type of sensor and the pin for sensor
sensor = Adafruit_DHT.DHT22
pin = 4

# Create an ApiClient object

api = ApiClient(token='ljGqF2u0ZCwHADAukMoE7shORQeD4O')

# Get a Ubidots Variable

try:
    variable1 = api.get_variable("57db89de7625425bd03a2f5e")
    variable2 = api.get_variable("57db8a007625425d9746e931")

except ValueError:
    print"It is not possible to obtain the variable"

while(1):
    try:
	humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
        value1 = random.randint(1, 100)
        variable1.save_value({'value': humidity})
        variable2.save_value({'value': temperature})

        print "Value sent"
        time.sleep(120)
    except ValueError:
        print "Value not sent"

