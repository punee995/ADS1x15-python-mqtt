import paho.mqtt.client as paho
import time
import Adafruit_ADS1x15

adc = Adafruit_ADS1x15.ADS1115()
#adc = Adafruit_ADS1x15.ADS1015()

# Choose a gain of 1 for reading voltages from 0 to 4.09V.
# Or pick a different gain to change the range of voltages that are read:
#  - 2/3 = +/-6.144V
#  -   1 = +/-4.096V
#  -   2 = +/-2.048V
#  -   4 = +/-1.024V
#  -   8 = +/-0.512V
#  -  16 = +/-0.256V
# See table 3 in the ADS1015/ADS1115 datasheet for more info on gain.
GAIN = 1



broker="127.0.0.1"
port=1883

client1= paho.Client("control1")                           #create client object
client1.connect(broker,port)                               #establish connection


while True:
	val = [0]*4
	for i in range(4):
		val[i] = adc.read_adc(i, gain=GAIN)   
	client1.publish("adc/ch0",val[0])
	client1.publish("adc/ch1",val[1])
	client1.publish("adc/ch2",val[2])
	client1.publish("adc/ch3",val[3])
	time.sleep(0.5)
