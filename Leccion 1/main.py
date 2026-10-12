from machine import Pin
from utime import sleep

# Importar librerías y configurar pines
in1 = Pin(19, Pin.OUT)        # LOZ ida
in2 = Pin(18, Pin.OUT)        # LOZ vuelta
in1.off()
in2.off()

T_MOVER = 1.4                   # s que se mueve el LOZ
T_DESCANSO = 2                # s que descansa

def parar():
    in1.off()
    in2.off()

def ida():
    in2.off()
    in1.on()

def vuelta():
    in1.off()
    in2.on()

# Ciclo fijo de la línea: ida 2 s, descansa 3 s, vuelta 2 s, descansa 3 s
print("Linea en marcha. Ctrl+C para detener")
try:
    while True:
        print("ida")
        ida()
        sleep(T_MOVER)

        print("descanso")
        parar()
        sleep(T_DESCANSO)

        print("vuelta")
        vuelta()
        sleep(T_MOVER)

        print("descanso")
        parar()
        sleep(T_DESCANSO)
except KeyboardInterrupt:
    parar()
    print("Linea detenida")
