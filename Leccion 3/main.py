from machine import Pin, PWM, ADC, time_pulse_us
from utime import sleep_ms, sleep_us, ticks_ms, ticks_diff

# Importar librerías y configurar pines
pot = ADC(Pin(34))            # potenciómetro 10K = perilla de velocidad
pot.atten(ADC.ATTN_11DB)      # lectura completa de 0 a 4095
in1 = PWM(Pin(19))            # LOZ (con PWM para regular velocidad)
in1.freq(1000)                # 1 kHz
in2 = Pin(18, Pin.OUT)        # LOZ vuelta: siempre apagado, un solo sentido
trig = Pin(4, Pin.OUT)        # ultrasónico mirando el aspa del molino
echo = Pin(5, Pin.IN)
led = Pin(26, Pin.OUT)        # parpadea cada vez que pasa un aspa
in1.duty(0)
in2.off()
led.off()

ASPAS = 1                     # aspas que ve el ultra por vuelta (1 o 2 funciona mejor)
UMBRAL = 10                   # cm: más cerca que esto = aspa frente al sensor
HISTERESIS = 3                # cm extra para decir "ya se fue el aspa"
VENTANA = 2000                # ms que contamos antes de calcular vueltas/s
MINIMO = 350                  # fuerza más baja que sí mueve el LOZ; ajústalo

# Definir funciones
def distancia_cm():
    trig.off()
    sleep_us(2)
    trig.on()
    sleep_us(10)
    trig.off()
    t = time_pulse_us(echo, 1, 6000)   # timeout corto: solo nos importa lo cercano
    if t < 0:
        return 100.0
    return (t * 0.0343) / 2

def fuerza_perilla():
    return pot.read() * 1023 // 4095    # 0 a 1023

def motor(fuerza):
    in2.off()
    if fuerza < MINIMO:
        in1.duty(0)
        return 0
    in1.duty(fuerza)
    return fuerza

# 1) La perilla pone la velocidad del LOZ
# 2) El ultra cuenta FLANCOS: aspa lejos -> aspa cerca = una pasada
# 3) Cada VENTANA ms: vueltas/s = pasadas / ASPAS / segundos
print("Tacometro del molino. Gira la perilla. Ctrl+C para detener")
aspa_cerca = False
pasadas = 0
inicio = ticks_ms()
try:
    while True:
        fuerza = motor(fuerza_perilla())

        cm = distancia_cm()
        if not aspa_cerca and cm < UMBRAL:
            aspa_cerca = True          # flanco: el aspa acaba de llegar
            pasadas += 1
            led.on()
        elif aspa_cerca and cm > UMBRAL + HISTERESIS:
            aspa_cerca = False         # el aspa ya se fue; esperamos la siguiente
            led.off()

        transcurrido = ticks_diff(ticks_ms(), inicio)
        if transcurrido >= VENTANA:
            segundos = transcurrido / 1000
            vps = pasadas / ASPAS / segundos
            print("velocidad", fuerza * 100 // 1023, "%  | pasadas", pasadas,
                  "| vueltas/s", round(vps, 2), "| rpm", round(vps * 60))
            pasadas = 0
            inicio = ticks_ms()

        sleep_ms(20)                   # ~25 lecturas por segundo
except KeyboardInterrupt:
    in1.duty(0)
    led.off()
    print("Molino detenido")
