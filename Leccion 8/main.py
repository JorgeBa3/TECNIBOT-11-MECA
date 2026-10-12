from machine import Pin, PWM, time_pulse_us
from utime import sleep, sleep_us

# Importar librerías y configurar pines
led = Pin(23, Pin.OUT)
buzzer = PWM(Pin(22))
in1 = Pin(19, Pin.OUT)        # LOZ ida
in2 = Pin(18, Pin.OUT)        # LOZ vuelta
trig = Pin(4, Pin.OUT)
echo = Pin(5, Pin.IN)
led.off()
buzzer.duty(0)
in1.off()
in2.off()
TIEMPO_TOPE = 4               # s hasta el final del riel; ajústalo
MARGEN = 3                    # se recalcula con el hueco entre centros
N_SEGUIR = 3                  # lecturas seguidas del mismo envase para llenar
modos = ["GRANDE", "MEDIANO", "CHICO"]
segundos = [3.0, 2.0, 1.0]
ya_lleno = False
visto = None
racha = 0

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

def kmeans(datos, k=3):
    n = len(datos)
    centros = [datos[0], datos[n // 3], datos[(2 * n) // 3]]
    for _ in range(8):
        grupos = [[] for _ in range(k)]
        for x in datos:
            d = [abs(x - c) for c in centros]
            grupos[d.index(min(d))].append(x)
        for i in range(k):
            if grupos[i]:
                centros[i] = sum(grupos[i]) / len(grupos[i])
    return centros

def parar():
    in1.off()
    in2.off()

def ida():
    in2.off()
    in1.on()

def vuelta():
    in1.off()
    in2.on()

def llenar(t):
    parar()
    led.on()
    buzzer.freq(2000)
    buzzer.duty(512)
    print("vaciando", t, "s")
    sleep(t)
    buzzer.duty(0)
    led.off()

def tiempo_de(cm, centros, etiqueta):
    d = [abs(cm - c) for c in centros]
    menor = min(d)
    idx = d.index(menor)
    if menor > MARGEN:
        return None, None, menor
    nombre = etiqueta[idx]
    t = segundos[modos.index(nombre)]
    return t, nombre, menor

# 1) Entrenar 3 envases (Enter cuando este listo) y K-means
archivo = open("datos.csv", "w")
archivo.write("cm,modo\n")
grupos = {"GRANDE": [], "MEDIANO": [], "CHICO": []}
print("Entrena 3 envases. Enter cuando el envase este bajo el ultra")
for modo in modos:
    print("Pon el envase", modo, "y pulsa Enter")
    input()
    sleep(1)
    for i in range(8):
        c = distancia_cm()
        print(i + 1, "cm=", round(c, 1))
        if c < 400:
            grupos[modo].append(c)
            archivo.write("{:.1f},{}\n".format(c, modo))
        sleep(0.15)
    if len(grupos[modo]) == 0:
        print("No leyo", modo, "- acercalo y vuelve a correr")
archivo.close()

datos = grupos["GRANDE"] + grupos["MEDIANO"] + grupos["CHICO"]
if min(len(grupos[m]) for m in modos) < 2:
    print("Faltaron lecturas (400). Acerca el ultra y vuelve a Run")
    while True:
        sleep(1)
centros = kmeans(datos, 3)
medias = {}
for modo in modos:
    pts = grupos[modo]
    medias[modo] = sum(pts) / len(pts)
etiqueta = []
usados = []
for c in centros:
    cand = sorted(modos, key=lambda m: abs(c - medias[m]))
    for m in cand:
        if m not in usados:
            etiqueta.append(m)
            usados.append(m)
            break
print("K-means centros:", centros)
orden = sorted(centros)
hueco = min(orden[1] - orden[0], orden[2] - orden[1])
MARGEN = hueco * 0.4
if MARGEN < 2:
    MARGEN = 2
print("etiquetas:", etiqueta, "margen=", round(MARGEN, 1), "cm")

# 2) Recorrido continuo: ida hasta el tope, luego vuelta
# 3) 3 ecos seguidos del mismo centro = envase; hueco = vacio y puede volver a llenar
sentido = "IDA"
t_tramo = 0.0
print("Recorrido")
while True:
    cm = distancia_cm()
    t, nombre, err = tiempo_de(cm, centros, etiqueta)
    if nombre is None:
        visto = None
        racha = 0
        ya_lleno = False
        print("vacio", "cm=", round(cm, 1))
    else:
        if nombre == visto:
            racha += 1
        else:
            visto = nombre
            racha = 1
            ya_lleno = False
        print(nombre, "cm=", round(cm, 1), "racha=", racha)
        if racha >= N_SEGUIR and not ya_lleno:
            print("llena", nombre, "error=", round(err, 1))
            llenar(t)
            ya_lleno = True
    if sentido == "IDA":
        ida()
    else:
        vuelta()
    t_tramo += 0.1
    if t_tramo >= TIEMPO_TOPE:
        parar()
        sleep(0.3)
        if sentido == "IDA":
            sentido = "VUELTA"
        else:
            sentido = "IDA"
        t_tramo = 0.0
        print("tope: regresa")
    sleep(0.08)
