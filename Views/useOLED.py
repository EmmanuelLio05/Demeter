import machine
import ssd1306
from time import sleep

class oseOLED:
    def __init__(self):
        self.i2c = machine.SoftI2C(scl=machine.Pin(22), sda=machine.Pin(21))
        self.pin = machine.Pin(16, machine.Pin.OUT)
        self.pin.value(0) #Configura GPIO16 en bajo para resetear el OLED
        self.pin.value(1) #Mientras que el OLED esté ejecutándose, GPIO16 debe estar en 1
        self.oled = ssd1306.SSD1306_I2C(128, 64, i2c)
        self.oled.fill(0)
        self.oled.show()
        self.aTemperature = [0x00, 0x00, 0x03, 0xc0, 0x02, 0x40, 0x02, 0x00, 0x02, 0x40, 0x02, 0x00, 0x02, 0x00, 0x02, 0x40,
                             0x02, 0x00, 0x02, 0x40, 0x06, 0x60, 0x05, 0xa0, 0x05, 0xa0, 0x06, 0x60, 0x03, 0xc0, 0x00, 0x00]
        self.aHumidity = [0x07, 0xe0, 0x0f, 0xf0, 0x18, 0x18, 0x30, 0x0c, 0x30, 0x0c, 0x20, 0x04, 0x20, 0x04, 0x30, 0x0c, 
	                      0x30, 0x0c, 0x18, 0x18, 0x0c, 0x30, 0x07, 0xe0, 0x04, 0x20, 0x06, 0x60, 0x02, 0x40, 0x03, 0xc0]
        self.aLight = [0x07, 0xe0, 0x0f, 0xf0, 0x18, 0x18, 0x30, 0x0c, 0x30, 0x0c, 0x20, 0x04, 0x20, 0x04, 0x30, 0x0c, 
	                   0x30, 0x0c, 0x18, 0x18, 0x0c, 0x30, 0x07, 0xe0, 0x04, 0x20, 0x06, 0x60, 0x02, 0x40, 0x03, 0xc0]

    def display_parameter(self, parameter, value):
        self.oled.text(0, 0, value)