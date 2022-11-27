import os
import time
import sys
sys.path.insert(0, '/libs')
import ufirebase as firebase


class useFirebase:
    def __init__(self):
        firebase.setURL("https://hermes-f3af7-default-rtdb.firebaseio.com/")
    
    def setTemperature(self,nTemperature):
        firebase.put("telemetry/temperature", nTemperature, bg=0)

    def setHumidity(self,nHumidity):
        firebase.put("telemetry/temperature", nHumidity, bg=0)

    def setBrightness(self,nBrightness):
        firebase.put("telemetry/temperature", nBrightness, bg=0)

    def setWater(self,nWater):
        firebase.put("control/water", nWater, bg=0)

    def getFan(self):
        firebase.get("control/fan", "bFan", bg=0)
        return firebase.bFan

    def getWater(self):
        firebase.get("control/fan", "bWater", bg=0)
        return firebase.bWater

    def getLight(self):
        firebase.get("control/light", "bLight", bg=0)
        return firebase.bLight
        