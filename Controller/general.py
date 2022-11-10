import network

def wifi_conecta():
    wlan = network.WLAN(network.STA_IF)
    wlan.active(True) #Activa el Wifi
    wlan.connect(ssid, password) #Hace la conexión
    while wlan.isconnected() == False: #Espera a que se conecte a la red pass
        print('Conexion con el WiFi %s establecida' % ssid)
        print(wlan.ifconfig()) #Muestra la IP y otros datos del Wi-Fi

