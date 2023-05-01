# Librerías
from machine import ADC, Pin
import network
import urequests
import json
import utelegram
import utime

# Configuración de los pines
led1 = Pin(2, Pin.OUT)
led2 = Pin(22, Pin.OUT)
led3 = Pin(4, Pin.OUT)
bombillo = Pin(19, Pin.OUT)
pot = ADC(Pin(34))
lm35 = ADC(Pin(35))

lm35.atten(ADC.ATTN_11DB)
lm35.width(ADC.WIDTH_12BIT)
pot.atten(ADC.ATTN_11DB)
pot.width(ADC.WIDTH_12BIT)

# Conexión con Wi-Fi
wifi_config = {
    'ssid':'BGNet_2.4G ETB',
    'password':'e85a17J04G18'
}

#wifi_config = {
#    'ssid':'ETITC-DOCENTES',
#    'password':'Navegar2018..'
#}

# Conexión con Bot de Telegram
utelegram_config = {
    'token': '6057458573:AAH1o_4UwqtQXy1e1Ql6w6ESR6RaUz98rXs'
}

wlan = network.WLAN(network.STA_IF)
wlan.active(True)
wlan.connect(wifi_config['ssid'], wifi_config['password'])
while not wlan.isconnected():
    pass
print("Conexión WiFi establecida!")

def voltajePot():
    return round(pot.read()*3.3/4095,2)

def temperaturaLM35():
    return round((lm35.read() * 3.3 / 4095 * 1000)/10,2)

## Funciones Bot Telegram:
def get_message(message):
    bot.send(message['message']['chat']['id'], "Escribe un comando válido o ingresa al menú")

def reply_ping(message):
    bot.send(message['message']['chat']['id'], 'pong')
    
def handleSubmit(message):
    url = "http://192.168.0.3/iotdatabase/insertDataESP32.php";
    
    data = {
        "led1on": led1.value(),
        "led2on": led2.value(),
        "led3on": led3.value(),
        "temperatura": temperaturaLM35(),
        "bombilloOn": bombillo.value()
    }
    headers = {'Content-Type': 'application/json'}
    
    response = urequests.post(url, json=data, headers=headers)
    
    data = json.loads(response.content)
    print(data)
    if(data == "ok"):
        bot.send(message['message']['chat']['id'], "Los datos han sido almacenados en la base de datos")
        
def led_handle(message):
    messageText = message['message']['text']
    if messageText == "/led1":
        led1.on()
        bot.send(message['message']['chat']['id'], "Led 1 encendido")
    elif messageText == "/led2":
        led2.on()
        bot.send(message['message']['chat']['id'], "Led 2 encendido")
    elif messageText == "/led3":
        led3.on()
        bot.send(message['message']['chat']['id'], "Led 3 encendido")
    elif messageText == "/led1off":
        led1.off()
        bot.send(message['message']['chat']['id'], "Led 1 apagado")
    elif messageText == "/led2off":
        led2.off()
        bot.send(message['message']['chat']['id'], "Led 2 apagado")
    elif messageText == "/led3off":
        led3.off()
        bot.send(message['message']['chat']['id'], "Led 3 apagado")
    elif messageText == "/bombillo":
        bombillo.on()
        bot.send(message['message']['chat']['id'], "Bombillo encendido")
    elif messageText == "/bombillooff":
        bombillo.off()
        bot.send(message['message']['chat']['id'], "Bombillo apagado")

def obtenerTemperatura(message):
    bot.send(message['message']['chat']['id'], "Temperatura: "+str(temperaturaLM35())+"°C")

def leerPot(message):
    bot.send(message['message']['chat']['id'], "Voltaje: "+str(voltajePot())+" V")

if wlan.isconnected():
    bot = utelegram.ubot(utelegram_config['token'])
    bot.register('/ping', reply_ping)
    bot.register('/led1', led_handle)
    bot.register('/led2', led_handle)
    bot.register('/led3', led_handle)
    bot.register('/led1off', led_handle)
    bot.register('/led2off', led_handle)
    bot.register('/led3off', led_handle)
    bot.register('/potenciometro', leerPot)
    bot.register('/bombillo', led_handle)
    bot.register('/bombillooff', led_handle)
    bot.register('/temperatura', obtenerTemperatura)
    bot.register('/guardardatos', handleSubmit)
    bot.set_default_handler(get_message)
    
    print('BOT LISTENING')
    bot.listen()
else:
    print('No conectado a WiFi')