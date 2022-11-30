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
RNG_LIGHT_START = (1,1,1,9,0,0,0,0) #Rango de funcionamiento de luz
RNG_LIGHT_END = (1,1,1,23,59,59,0,0)
RNG_FAN_START = (1,1,1,15,0,0,0,0) #Rango de funcionamiento de ventilador
RNG_FAN_END = (1,1,1,23,59,59,0,0)

pWater1 = Pin(12,mode=Pin.OUT) #Pines para bomba de agua
pWater2 = Pin(13,mode=Pin.OUT)
pFan1 = Pin(26,mode=Pin.OUT) #Pines para ventilador
pFan2 = Pin(27,mode=Pin.OUT)
pLight = Pin(25,mode=Pin.OUT, value=1) #Pin para luz

def wifi_conecta(): #Funcion para conectar a wifi
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True) #Activa el Wifi
    ssid ='Megacable_2.4G_C5A6'
    wlan.connect('Megacable_2.4G_C5A6', 'EbqCXMFE') #Hace la conexión
    while wlan.isconnected() == False: #Espera a que se conecte a la red pass
        print('Conexion con el WiFi %s establecida' % ssid)
        print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi

def control_Light(bHermes_Light): #Funcion para conectar luz
    current_time = time.gmtime() #Se obtiene tiempo acual
    if (bHermes_Light==True): #Se valida estado en firebase
        if(current_time[3]>=RNG_LIGHT_START[3] and current_time[4]>=RNG_LIGHT_START[4] and current_time[5]>=RNG_LIGHT_START[5]): #Se valida rango
            if(current_time[3]<=RNG_LIGHT_END[3] and current_time[4]<=RNG_LIGHT_END[4] and current_time[5]<=RNG_LIGHT_END[5]):
                pLight.off() #Se enciende
                return
    pLight.on() #Se apaga

def control_Fan(bHermes_Fan): #Funcion para conectar ventilador
    current_time = time.gmtime()#Se obtiene tiempo acual
    if (bHermes_Fan==True): #Se valida estado en firebase
        if(current_time[3]>=RNG_FAN_START[3] and current_time[4]>=RNG_FAN_START[4] and current_time[5]>=RNG_FAN_START[5]):#Se valida rango
            if(current_time[3]<=RNG_FAN_END[3] and current_time[4]<=RNG_FAN_END[4] and current_time[5]<=RNG_FAN_END[5]):
                pFan1.off()#Se enciende
                pFan2.on()
                return
    pFan1.off()#Se apaga
    pFan2.off()

def control_Water(nHermes_Water): #Funcion para conectar bomba de agua
    fire = useFirebase()
    pWater1.on()#Se enciende
    pWater2.off()
    time.sleep(nHermes_Water) #Duerme el tiempo indicado
    pWater1.off()#Se apaga
    pWater2.off()
    fire.setWater(0) #Se regresa valor a 0 en firebase
