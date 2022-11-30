import machine
from machine import ADC, Pin
from time import sleep

class usePhotoR: #Clase de uso de ldr
    def __init__(self):
        self.ldr = ADC(Pin(34, mode=Pin.IN))
        self.ldr.atten(ADC.ATTN_11DB)

    def getLight(self): #obtiene el valor de LDR
        ldr_vl = 0
        nIntents = 5
        while nIntents > 0:
            ldr_vl = self.ldr.read()
            nIntents = nIntents - 1
        return ldr_vl
