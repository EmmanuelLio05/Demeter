import os
import time
import sys
sys.path.insert(0, '/libs')
import ufirebase as firebase

class useFirebase: #Clase de uso de firebase
    def __init__(self):
        firebase.setURL("https://hermes-f3af7-default-rtdb.firebaseio.com/")
    
    def setTemperature(self,nTemperature): #setea temperatura
        firebase.put("telemetry/temperature", nTemperature, bg=0)

    def setHumidity(self,nHumidity): #setea humedad
        firebase.put("telemetry/humidity", nHumidity, bg=0)

    def setBrightness(self,nBrightness): #setea brillo
        firebase.put("telemetry/brightness", nBrightness, bg=0)

    def getFan(self): #obtiene estado de ventilador
        firebase.get("control/fan", "bFan", bg=0)
        return firebase.bFan

    def getWater(self): #obtiene estado de agua
        firebase.get("control/Water", "bWater", bg=0)
        return firebase.bWater

    def getLight(self): #obtiene luz
        firebase.get("control/light", "bLight", bg=0)
        return firebase.bLight
        
    def setFan(self, bFan): #setea ventilador
        firebase.put("control/fan", bFan, bg=0)

    def setWater(self, nWater): #setea bomba de agua
        firebase.put("control/water", nWater, bg=0)

    def setLight(self, bLight): #setea luz
        firebase.put("control/light", bLight, bg=0)