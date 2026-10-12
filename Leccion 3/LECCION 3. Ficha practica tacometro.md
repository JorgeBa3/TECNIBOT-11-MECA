LECCIÓN 3. Tacómetro del molino: ficha práctica

Descripción: La perilla (potenciómetro 10K) regula la velocidad del LOZ con PWM. En el eje del LOZ va un molino. El ultrasónico mira el aspa de frente: cada vez que pasa, cuenta una pasada. Cada 2 s la consola muestra la velocidad (%), las pasadas, las vueltas por segundo y las rpm. La LED parpadea con cada aspa.

Electrónica:

Materiales:
ESP32
Protoboard
Motor LOZ con su driver
Molino de 1 o 2 aspas anchas (cartón, K'NEX o impreso) en el eje del LOZ
Potenciómetro 10K
Sensor ultrasónico HC-SR04
LED
Resistencia 220 Ω
Cables jumper

Paso 1: Potenciómetro.
Pata izquierda → 3.3V, pata del medio → GPIO 34, pata derecha → GND

Paso 2: LOZ en el driver.
I/D del driver → GPIO 19 (con PWM) y GPIO 18 (siempre apagado, un solo sentido).

Paso 3: Ultrasónico mirando el molino.
VCC → 5V, GND → GND, TRIG → GPIO 4, ECHO → GPIO 5
Colócalo de frente a donde pasa el aspa, a unos 4–6 cm. Cuando NO hay aspa, detrás debe quedar espacio libre (más de 15 cm) o una pared lejana.

Paso 4: LED.
GPIO 26 → 220 Ω → (+), (−) → GND

Paso 5: USB a la computadora.

Programación:
Sube main.py. Consola de Thonny.

Importar librerías y configurar pines:
Perilla 34, LOZ 19/18, ultra 4/5, LED 26. ASPAS = 1, UMBRAL = 10 cm, VENTANA = 2000 ms, MINIMO = 350.

Definir funciones:
distancia_cm() con timeout corto. fuerza_perilla() convierte 0–4095 a 0–1023. motor() pone el PWM y lo apaga debajo de MINIMO.

# 1) La perilla pone la velocidad. Si el LOZ zumba y no gira, sube MINIMO.

# 2) Cada flanco LEJOS → CERCA es una pasada de aspa; la LED parpadea. Si la LED no parpadea, acerca el ultra o sube UMBRAL. Si parpadea sin aspa, baja UMBRAL.

# 3) Cada 2 s: vueltas/s = pasadas ÷ ASPAS ÷ segundos, y rpm = vueltas/s × 60. Si tu molino tiene 2 aspas, cambia ASPAS = 2.

Problemas comunes:
- Marca 0 vueltas con el molino girando: el aspa es muy delgada o está lejos; el ultra no recibe eco. Usa un aspa ancha y plana.
- Marca menos vueltas al subir mucho la velocidad: el aspa pasa más rápido de lo que el ultra alcanza a leer. Baja la velocidad o usa 1 sola aspa.
