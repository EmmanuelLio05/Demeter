import sys
sys.path.insert(0, '/Controller/uses')
sys.path.insert(0, '/Views')
sys.path.insert(0, '/Controller/firebase')
sys.path.insert(0, '/Controller')
#   AIzaSyArYBNdSGEe9Oi2Ls8xzCm0Hkxqn5HBLbg
from useDHT import useDHT
from usePhotoR import usePhotoR
from machine import Pin,PWM
from time import sleep
from useOLED import useOLED
from useFirebase import useFirebase
import general

#oled = useOLED()
dht = useDHT()
dht.doMeasure()
ldr = usePhotoR()
general.wifi_conecta()
fire = useFirebase()
while True:
    dht.doMeasure()
    t = dht.getTemperature()
    h = dht.getHumidity()
    l=ldr.getLight()
    fire.setTemperature(t)
    fire.setHumidity(h)
    fire.setBrightness(l)    
    general.control_Light(bool(fire.getLight()))
    general.control_Fan(bool(fire.getFan()))