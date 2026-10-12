from machine import Pin, PWM, time_pulse_us
from utime import sleep, sleep_us

# Importar librerías y configurar pines
trig = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)
servo = PWM(Pin(23))
led = Pin(26, Pin.OUT)
servo.freq(50)
led.off()
LIMITE = 50                   # cm: más lejos = nadie
PASO = 15
G_MIN = 20
G_MAX = 160
g = 90
DIR = 1                       # 1 = aumentando, -1 = disminuyendo

# Definir funciones
def angulo(grados):
    us = 500 + (grados / 180.0) * 2000
    d = int(us / 20000.0 * 1023)
    if d < 26:
        d = 26
    if d > 128:
        d = 128
    servo.duty(d)

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

def medir_en(grados):
    angulo(grados)
    sleep(0.25)
    return distancia_cm()

def hay(cm):
    return 5 < cm < LIMITE

angulo(g)
sleep(0.5)

# 1) Si no hay nadie, barre buscando (tipo péndulo, sin saltos)
# 2) Si hay presencia, mira un poco izq/der y se queda en el angulo mas cercano
# 3) Si se aleja, sigue el barrido desde donde se quedó, respetando la última dirección
while True:
    cm = medir_en(g)
    if hay(cm):
        led.on()
        print("sigue ang=", g, "cm=", round(cm, 1))
        cand = [g]
        if g - PASO >= G_MIN:
            cand.append(g - PASO)
        if g + PASO <= G_MAX:
            cand.append(g + PASO)
        mejor_g = g
        mejor_cm = cm
        for a in cand:
            d = medir_en(a)
            if hay(d) and d < mejor_cm:
                mejor_cm = d
                mejor_g = a

        # actualizar dirección según hacia dónde se movió al seguir a la persona
        if mejor_g > g:
            DIR = 1
        elif mejor_g < g:
            DIR = -1
        # si mejor_g == g, se mantiene la última DIR (no la reseteamos)

        g = mejor_g
        angulo(g)
    else:
        led.off()
        print("busca ang=", g, "cm=", round(cm, 1))
        g = g + PASO * DIR
        if g >= G_MAX:
            g = G_MAX
            DIR = -1
        elif g <= G_MIN:
            g = G_MIN
            DIR = 1
        angulo(g)
        sleep(0.15)