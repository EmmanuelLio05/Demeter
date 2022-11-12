import network
from machine import Pin

LIGHT_TOPIC = 'demeter.control.light'
WATER_TOPIC = 'demeter.control.water'
FAN_TOPIC = 'demeter.control.fan'
TEMPERATURE_TOPIC = 'demeter.telemetry.temperature'
HUMIDITY_TOPIC = 'demeter.telemetry.humidity'
BRIGHTNESS_TOPIC = 'demeter.telemetry.brightness'

pWater = Pin(2,mode=Pin.OUT, value=1)
pFan = Pin(4,mode=Pin.OUT, value=1)
pLight = Pin(5,mode=Pin.OUT, value=1)

def wifi_conecta():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True) #Activa el Wifi
    wlan.connect('Megacable_2.4G_C5A6', 'EbqCXMFE') #Hace la conexión
    while wlan.isconnected() == False: #Espera a que se conecte a la red pass
        print('Conexion con el WiFi %s establecida' % ssid)
        print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi

def subscribe_handler(topic,msg):
    if topic == LIGHT_TOPIC:
        if msg == b'1':
            pLight.value(1)
        else:
            pLight.value(0)
    if topic == WATER_TOPIC:
        if msg == b'1':
            pWater.value(1)
        else:
            pWater.value(0)
    if topic == FAN_TOPIC:
        if msg == b'1':
            pFan.value(1)
        else:
            pFan.value(0)
