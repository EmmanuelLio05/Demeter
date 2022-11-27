import machine
from machine import Pin
from time import sleep
from dht import DHT11

class useDHT:
    def __init__(self):
        self.sensor = DHT11(Pin(14)) #Configura el DHT11 en el pin 14

    def doMeasure(self):
        b = True
        
        while b:
            try:
                self.sensor.measure() #Mide
                sleep(2)
                b = False
            except Exception as e:
                print(str(e))
    
    def getTemperature(self):
        return self.sensor.temperature()

    def getHumidity(self):
        hum = self.sensor.humidity()
        return hum