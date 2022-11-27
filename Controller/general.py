import sys
import network
from machine import Pin
import time
sys.path.insert(0, '/Controller/firebase')
from useFirebase import useFirebase

LIGHT_TOPIC = 'demeter.control.light'
WATER_TOPIC = 'demeter.control.water'
FAN_TOPIC = 'demeter.control.fan'
TEMPERATURE_TOPIC = 'demeter.telemetry.temperature'
HUMIDITY_TOPIC = 'demeter.telemetry.humidity'
BRIGHTNESS_TOPIC = 'demeter.telemetry.brightness'
RNG_LIGHT_START = (1,1,1,9,0,0,0,0)
RNG_LIGHT_END = (1,1,1,19,59,59,0,0)
RNG_FAN_START = (1,1,1,15,0,0,0,0)
RNG_FAN_END = (1,1,1,17,59,59,0,0)

pWater1 = Pin(12,mode=Pin.OUT)
pWater2 = Pin(13,mode=Pin.OUT)
pFan1 = Pin(26,mode=Pin.OUT)
pFan2 = Pin(27,mode=Pin.OUT)
pLight = Pin(25,mode=Pin.OUT, value=1)

def wifi_conecta():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True) #Activa el Wifi
    ssid ='Megacable_2.4G_C5A6'
    wlan.connect('Megacable_2.4G_C5A6', 'EbqCXMFE') #Hace la conexión
    while wlan.isconnected() == False: #Espera a que se conecte a la red pass
        print('Conexion con el WiFi %s establecida' % ssid)
        print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi

def control_Light(bHermes_Light):
    current_time = time.gmtime()
    if (bHermes_Light==True):
        if(current_time[3]>=RNG_LIGHT_START[3] and current_time[4]>=RNG_LIGHT_START[4] and current_time[5]>=RNG_LIGHT_START[5]):
            if(current_time[3]<=RNG_LIGHT_END[3] and current_time[4]<=RNG_LIGHT_END[4] and current_time[5]<=RNG_LIGHT_END[5]):
                pLight.off()
                return
    pLight.on()

def control_Fan(bHermes_Fan):
    current_time = time.gmtime()
    if (bHermes_Fan==True):
        if(current_time[3]>=RNG_FAN_START[3] and current_time[4]>=RNG_FAN_START[4] and current_time[5]>=RNG_FAN_START[5]):
            if(current_time[3]<=RNG_FAN_END[3] and current_time[4]<=RNG_FAN_END[4] and current_time[5]<=RNG_FAN_END[5]):
                pFan1.on()
                pFan2.off()
                return
    pFan1.off()
    pFan2.off()

def control_Water(nHermes_Water):
    fire = useFirebase()
    pWater1.on()
    pWater2.off()
    time.sleep(nHermes_Water)
    pWater1.off()
    pWater2.off()
    fire.setBrightness(0)
