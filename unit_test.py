import RPi.GPIO as GPIO
import Adafruit_DHT

#GPIO.setmode(GPIO.BCM)
#GPIO.setwarnings(True)
#GPIO.setup([1,2,3],GPIO.OUT)
#print ("Pin 1 " + GPIO.input(1))
#GPIO.output([1,2,3],(GPIO.LOW, GPIO.LOW, GPIO.HIGH))
#GPIO.output([1,2,3],GPIO.HIGH)

sensor = Adafruit_DHT.DHT22
humidity, temp = Adafruit_DHT.read_retry(sensor,3)
print (str(humidity) + "%")
print (str(temp) + "C")
