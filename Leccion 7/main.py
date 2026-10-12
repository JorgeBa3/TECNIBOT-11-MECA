from machine import Pin, SoftI2C
from mpu6050 import MPU6050
from utime import sleep
import math

# Importar librerías y configurar pines
i2c = SoftI2C(scl=Pin(22), sda=Pin(21), freq=100000)
print("I2C scan:", i2c.scan())
mpu = MPU6050(i2c)
in1 = Pin(19, Pin.OUT)        # LOZ adelante
in2 = Pin(18, Pin.OUT)        # LOZ atrás
in1.off()
in2.off()

POSES = ["IZQUIERDA", "DERECHA", "HORIZONTAL"]
N_MUESTRAS = 10               # lecturas por pose al entrenar
N_SEGUIR = 3                  # lecturas seguidas iguales para cambiar de orden

# Definir funciones
def angulos():
    # Inclinación del control en los dos ejes (X e Y), en grados
    ax, ay, az, gx, gy, gz = mpu.leer()
    ang_x = math.atan2(ax, math.sqrt(ay * ay + az * az)) * 180 / math.pi
    ang_y = math.atan2(ay, math.sqrt(ax * ax + az * az)) * 180 / math.pi
    return ang_x, ang_y

def distancia(p, c):
    return math.sqrt((p[0] - c[0]) ** 2 + (p[1] - c[1]) ** 2)

def cercano(p, centros):
    d = [distancia(p, c) for c in centros]
    return d.index(min(d))

def kmeans(datos, centros):
    for _ in range(10):
        grupos = [[] for _ in centros]
        for p in datos:
            grupos[cercano(p, centros)].append(p)
        for i in range(len(centros)):
            if grupos[i]:
                sx = sum(p[0] for p in grupos[i])
                sy = sum(p[1] for p in grupos[i])
                centros[i] = (sx / len(grupos[i]), sy / len(grupos[i]))
    return centros

def parar():
    in1.off()
    in2.off()

def adelante():
    in2.off()
    in1.on()

def atras():
    in1.off()
    in2.on()

# 1) Entrenar: el alumno inclina el control en cada pose
print("=== CARRO A CONTROL REMOTO: entrenamiento ===")
datos = []
etiquetas = []
for pose in POSES:
    print("Inclina el control hacia", pose, "y pulsa Enter (muévelo un poquito mientras mide)")
    input()
    for _ in range(N_MUESTRAS):
        p = angulos()
        datos.append(p)
        etiquetas.append(pose)
        sleep(0.1)
    print(pose, "listo:", round(p[0], 1), round(p[1], 1))

# 2) K-means con 3 centros (empieza en la primera lectura de cada pose)
centros = kmeans(datos, [datos[0], datos[N_MUESTRAS], datos[2 * N_MUESTRAS]])

# 3) Ponerle nombre a cada centro: gana la pose que más cayó en él
nombres = []
for i in range(3):
    votos = {pose: 0 for pose in POSES}
    for p, e in zip(datos, etiquetas):
        if cercano(p, centros) == i:
            votos[e] += 1
    nombre = max(votos, key=votos.get)
    nombres.append(nombre)
    print("centro", i, "=", nombre, "(", round(centros[i][0], 1), ",", round(centros[i][1], 1), ")", votos)

if len(set(nombres)) < 3:
    print("OJO: dos poses quedaron en el mismo centro. Inclina más y vuelve a entrenar.")

# 4) Manejar: izquierda = adelante, derecha = atrás, horizontal = parado
print("=== A manejar! Ctrl+C para detener ===")
orden = "HORIZONTAL"
visto = None
racha = 0
try:
    while True:
        pose = nombres[cercano(angulos(), centros)]
        if pose == visto:
            racha += 1
        else:
            visto = pose
            racha = 1
        if racha >= N_SEGUIR and pose != orden:
            orden = pose
            parar()
            sleep(0.1)                # respiro antes de cambiar de sentido
            if orden == "IZQUIERDA":
                adelante()
            elif orden == "DERECHA":
                atras()
            print("control:", orden)
        sleep(0.1)
except KeyboardInterrupt:
    parar()
    print("Carro detenido")
