from machine import Pin, time_pulse_us
from utime import sleep, sleep_us

# Importar librerías y configurar pines
led = Pin(26, Pin.OUT)
motor = Pin(18, Pin.OUT)      # base transistor NPN → banda ON/OFF
trig = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)
led.off()
motor.off()
CERCA = 25                    # cm: hay pieza delante
TIEMPO = 2                    # s que corre la banda por pieza
ya_ciclo = False

# Definir funciones
def distancia_cm():
    trig.off()
    sleep_us(2)
    trig.on()
    sleep_us(10)
    trig.off()
    t = time_pulse_us(echo, 1, 30000)
    if t < 0:
        return 400.0
    cm = (t * 0.0343) / 2
    if cm < 2 or cm > 400:
        return 400.0
    return cm

def parar():
    motor.off()
    led.off()

def producir():
    motor.on()
    led.on()
    sleep(TIEMPO)
    parar()

# 1) Medir si hay pieza delante (CERCA / LEJOS)
# 2) CERCA: un ciclo de banda; LEJOS: no gastes motor
# 3) Quita la pieza para poder detectar la siguiente
while True:
    cm = distancia_cm()
    cerca = 5 < cm < CERCA
    if cerca:
        print("CERCA cm=", round(cm, 1))
        if not ya_ciclo:
            print("produce", TIEMPO, "s")
            producir()
            ya_ciclo = True
    else:
        parar()
        ya_ciclo = False
        print("LEJOS cm=", round(cm, 1))
    sleep(0.1)
