from machine import Pin, PWM, ADC
from utime import sleep

# Importar librerías y configurar pines
pot = ADC(Pin(34))            # potenciómetro 10K = perilla de velocidad
pot.atten(ADC.ATTN_11DB)      # lectura completa de 0 a 4095
in1 = PWM(Pin(19))            # LOZ ida (con PWM para regular velocidad)
in1.freq(1000)                # 1 kHz
in2 = Pin(18, Pin.OUT)        # LOZ vuelta: siempre apagado, un solo sentido
in2.off()
in1.duty(0)

MINIMO = 350                  # por debajo de esto el LOZ zumba pero no gira; ajústalo

def parar():
    in1.duty(0)

def producir(fuerza):
    in2.off()
    in1.duty(fuerza)

# La perilla decide qué tan rápido produce la línea
print("Gira la perilla para cambiar la velocidad. Ctrl+C para detener")
try:
    while True:
        lectura = pot.read()                  # 0 a 4095
        fuerza = lectura * 1023 // 4095       # lo convertimos a 0 a 1023
        if fuerza < MINIMO:
            parar()
            print("perilla:", lectura, "-> linea detenida")
        else:
            producir(fuerza)
            print("perilla:", lectura, "-> velocidad", fuerza * 100 // 1023, "%")
        sleep(0.2)
except KeyboardInterrupt:
    parar()
    print("Linea detenida")
