#Objetivo: Leer el DHT y mostrar los datos obtenidos en la pantalla OLED
#Participantes: Magaly Idolisa Rojas Silva, Emilio Emmanuel Hernández Padilla Karina Guadalupe De Leon Fuentes


import machine
from machine import Pin
import ssd1306
from time import sleep
from dht import DHT11

i2c = machine.SoftI2C(scl=machine.Pin(22),sda=machine.Pin(21))
pin = machine.Pin(16, machine.Pin.OUT)
pin.value(0) #Configura GPIO16 en bajo para resetear el OLED
pin.value(1) #Mientras que el OLED esté ejecutándose, GPIO16 debe estar en 1
oled_ancho = 128
oled_alto = 64
oled = ssd1306.SSD1306_I2C(oled_ancho, oled_alto, i2c)
sensor = DHT11(Pin(14)) #Configura el DHT11 en el pin 14
while True:
    try:
        oled.fill(0)
        sleep(2)#Espera 2 segundos para no saturar el DHT
        sensor.measure() #Mide
        temp_c = sensor.temperature() #Obtiene la temperatura
        hum = sensor.humidity() #Obtiene la humedad
        print(str(temp_c))
        oled.text(str(temp_c) + " C",0,0)
        oled.text(str(hum) + "%",0,00)
        oled.show()
    except Exception as e:
        print(str(e))