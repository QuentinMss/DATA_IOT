from machine import Pin, PWM # importe dans le code la lib qui permet de gerer les Pin de sortie et de modulation du signal
import network   #import des fonction lier au wifi
import urequests #import des fonction lier au requetes http
import utime #import des fonction lier au temps
import ujson #import des fonction lier aà la convertion en Json

led = [PWM(Pin(12,mode=Pin.OUT)),PWM(Pin(13,mode=Pin.OUT)),PWM(Pin(14,mode=Pin.OUT))]

for i in led:
    i.freq(1_000)
    i.duty_u16(30000)

maison = {
    "Gryffindor": [0,0,255],
    "Hufflepuff": [255,255,0],
    "Ravenclaw": [255,0,0],
    "Slytherin": [0,255,0]
}

def setColor(c):
    for i in range(3):
        led[i].duty_u16(c[i]*256)


wlan = network.WLAN(network.STA_IF) # met la raspi en mode client wifi
wlan.active(True) # active le mode client wifi
ssid = ''
password = ''
wlan.connect(ssid, password) # connecte la raspi au réseau
url = "https://hp-api.lainocs.fr/characters/harry-potter"
#http://date.jsontest.com/
while not wlan.isconnected():
    print("pas co")
    utime.sleep(1)
    pass

while(True):
    try:
        r = urequests.get(url) # lance une requete sur l'url
        print(r.json()["house"]) # traite sa reponse en Json
        house = r.json()["house"]
        setColor(maison[house])
        r.close() # ferme la demande
        utime.sleep(1)
    except Exception as e:
        print(e)