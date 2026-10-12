from machine import Pin
from utime import sleep

# Importar librerías y configurar pines
in1 = Pin(19, Pin.OUT)        # LOZ adelante
in2 = Pin(18, Pin.OUT)        # LOZ atrás: siempre apagado
in1.off()
in2.off()

# Definir funciones
def parar():
    in1.off()
    in2.off()

def girar():
    in2.off()
    in1.on()

# El LOZ gira sin parar hasta que presiones Ctrl+C
print("Motor girando. Ctrl+C para detener")
girar()
try:
    while True:
        sleep(1)
except KeyboardInterrupt:
    parar()
    print("Motor detenido")
