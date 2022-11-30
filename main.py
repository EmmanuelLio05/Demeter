import sys #Se importa sys
#Se insertan las carpetas necesarias para el loop
sys.path.insert(0, '/Controller/uses')
sys.path.insert(0, '/Views')
sys.path.insert(0, '/Controller/firebase')
sys.path.insert(0, '/Controller')
#   AIzaSyArYBNdSGEe9Oi2Ls8xzCm0Hkxqn5HBLbg
#Se importan las clases de los sensores y actuadores.
from useDHT import useDHT #clase DHT
from usePhotoR import usePhotoR #Clase ldr
from machine import Pin,PWM #Clases de machine
from time import sleep # funcion sleep
from useOLED import useOLED #clase del uso del oled
from useFirebase import useFirebase #clase de uso de firebase
import general #modulo general que contienen las funciones de control de actuadores

oled = useOLED() #instancia del oled
dht = useDHT() #instancia del DHT
dht.doMeasure() #Se mide el DHT
ldr = usePhotoR() #instancia del ldr
general.wifi_conecta() #se conecta a wifi
fire = useFirebase() #Instancia de firebase

while True: #LOOP
    dht.doMeasure()#Se mide el DHT
    t = dht.getTemperature() #Se obtienen las medidas del DHT
    h = dht.getHumidity()
    l=ldr.getLight() #Se obtiene la medida del LDR
    print(str(l))
    print(str(t))
    #Se sube la telemetría
    fire.setTemperature(t) 
    fire.setHumidity(h)
    fire.setBrightness(l)
    #Se controlan los actuadores
    general.control_Light(bool(fire.getLight()))
    general.control_Fan(bool(fire.getFan()))
    general.controlWater(fire.getWater())
    print('loop')
    