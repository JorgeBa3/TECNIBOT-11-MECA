LECCIÓN 8. Dosificador: el carrito llena y sigue

Descripción: El LOZ lleva el carrito de ida y vuelta. Entrenás 3 envases con el ultrasónico; cada distancia es un tiempo de llenado (3 s, 2 s, 1 s). Si hay envase, para, LED y buzzer. Si no, sigue. En el tope (tiempo) regresa.

Electrónica:

Materiales:
ESP32
Protoboard
Motor LOZ con su driver
Sensor ultrasónico HC-SR04
LED
Resistencia 220 Ω
Buzzer
Cables jumper
Carrito / riel K’NEX

Paso 1: Ultrasónico mirando el envase (abajo o al lado de la estación).
VCC → 5V, GND → GND, TRIG → GPIO 4, ECHO → GPIO 5

Paso 2: LOZ, LED y buzzer. USB a la computadora.
LOZ: I/D del driver → GPIO 19 (ida) y GPIO 18 (vuelta). HIGH/LOW, sin PWM.
LED: GPIO 26 → 220 Ω → (+), (−) → GND
Buzzer: GPIO 25 → (+), (−) → GND

Programación:
Sube main.py. Consola de Thonny.

Importar librerías y configurar pines:
LOZ 19/18, ultra 4/5, LED 26, buzzer 25. TIEMPO_TOPE = 4 (ajústalo al largo del riel).

Definir funciones:
distancia_cm() con timeout. llenar() para el LOZ, enciende LED y buzzer el tiempo del envase. tiempo_de() elige el centro más cercano.

# 1) Tres envases: GRANDE, MEDIANO, CHICO bajo el ultra. 3 s / 2 s / 1 s de vaciado.

# 2) El carrito recorre. TIEMPO_TOPE → regresa. Cruza 18 y 19 si el sentido sale al revés.

# 3) Envase cerca de un centro → una parada de llenado. Al quitarlo, puede volver a llenar. Sin envase (cm alto o 400) no para.
