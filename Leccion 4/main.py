from machine import Pin, PWM, time_pulse_us
from utime import sleep, sleep_us

# Importar librerías y configurar pines
led = Pin(26, Pin.OUT)
in1 = PWM(Pin(19))            # LOZ banda (con PWM para regular velocidad)
in1.freq(1000)                # 1 kHz
in2 = Pin(18, Pin.OUT)        # LOZ vuelta: siempre apagado, un solo sentido
trig = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)
led.off()
in1.duty(0)
in2.off()

LEJOS = 40                    # cm: más lejos que esto, la banda va a toda velocidad
PARADA = 9                    # cm: la pieza llegó al final, la banda se detiene
MINIMO = 350                  # fuerza más baja que sí mueve el LOZ; ajústalo
MAXIMO = 1023                 # fuerza a toda velocidad

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

def distancia_promedio():
    # 3 lecturas para que la velocidad no tiemble
    s = 0.0
    for _ in range(3):
        s += distancia_cm()
        sleep(0.02)
    return s / 3

def parar():
    in1.duty(0)

def banda(fuerza):
    in2.off()
    in1.duty(fuerza)

def fuerza_por_distancia(cm):
    # Regla de tres: de PARADA (lento) a LEJOS (rápido)
    return MINIMO + (cm - PARADA) * (MAXIMO - MINIMO) // (LEJOS - PARADA)

# 1) Medir a qué distancia está la pieza en la banda
# 2) LEJOS o sin pieza: toda velocidad
# 3) Acercándose: más cerca = más lento, para que no se caiga
# 4) Llegó al final (PARADA): la banda se detiene. Quita la pieza para seguir
print("Banda en marcha. Ctrl+C para detener")
try:
    while True:
        cm = distancia_promedio()
        if cm <= PARADA:
            parar()
            led.on()
            print("LLEGO cm=", round(cm, 1), "-> banda detenida, quita la pieza")
        elif cm >= LEJOS:
            banda(MAXIMO)
            led.off()
            print("LEJOS cm=", round(cm, 1), "-> velocidad 100 %")
        else:
            fuerza = int(fuerza_por_distancia(cm))
            banda(fuerza)
            led.on()
            print("CERCA cm=", round(cm, 1), "-> velocidad", fuerza * 100 // MAXIMO, "%")
        sleep(0.1)
except KeyboardInterrupt:
    parar()
    led.off()
    print("Banda detenida")
