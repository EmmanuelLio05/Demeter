import sys
sys.path.insert(0, '/Controller')

from umqtt.simple import MQTTClient
import general

class useMQTT:
    def __init__(self):
        self.SERVER = 'mqtt3.thingspeak.com'
        self.PUERTO = 1883
        self.ID_CANAL = '1897071' #Aquí pondremos los datos de ThingSpeak
        self.USUARIO = 'ISUQIBUjNzcnLBwhFC8JEwQ'
        self.ID_CLIENTE = 'ISUQIBUjNzcnLBwhFC8JEwQ'
        self.ID_PSWD ='CKj47v1TW6y5SEuwz1q1MRyy'
        self.cliente = MQTTClient(self.ID_CLIENTE, self.SERVER, self.PUERTO, self.USUARIO, self.ID_PSWD)
        self.cliente.connect()
        self.set_callback(general.subscribe_handler)
    
    def susbscribe_To_All(self):
        self.cliente.subscribe(general.BRIGHTNESS_TOPIC)
        self.cliente.subscribe(general.FAN_TOPIC)
        self.cliente.subscribe(general.HUMIDITY_TOPIC)
        self.cliente.subscribe(general.LIGHT_TOPIC)
        self.cliente.subscribe(general.TEMPERATURE_TOPIC)
        self.cliente.subscribe(general.WATER_TOPIC)

    def publish(self,topic,message):
        self.cliente.publish(topic,message)

