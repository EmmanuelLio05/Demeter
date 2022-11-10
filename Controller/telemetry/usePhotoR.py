import machine
from machine import ADC, Pin
from time import sleep

class usePhotoR:
    def __init__(self):
        self.ldr = ADC(Pin(34))
        self.ldr.atten(ADC.ATTN_11DB)

    def getLight(self):
        ldr_vl = 0
        while ldr_vl == 0:
            ldr_vl = self.ldr.read()
        return ldr_vl 
