# Plan del libro — Tecnibot 11 Mecatrónica (Smart Factory)

Público: 5.º bachillerato, grupos de 4–5, **40 minutos**, kit TK + **motor DC 3 V** (no LOZ).
Todo el código corre en la **ESP32** (MicroPython): sin sklearn, sin YOLO, sin PC para entrenar.

Este libro no es la Smart House de 4.º MECA ni la L8 de 5.º IA estirada a ocho clases. La casa y el LOZ ya se vieron. Aquí la línea **produce**: un molino o una banda que gira o para. El GPIO no alimenta el motor; un transistor abre o cierra el 3V3. El ML otra vez es semilla, pero la salida siempre es el mecanismo: umbral → AND → pieza → **cadencia (hélices/s)** → salud MPU → recta de demanda → dos modelos + OEE.

---

## Cómo se ve una clase (40 min)

| Min | Qué pasa |
|---|---|
| 0–5 | Punto de partida + 1 concepto (voz de estudiante, fábrica) |
| 5–13 | Electrónica: **2 pasos de armado** (como las fichas de 5.º IA) |
| 13–35 | Programación en bloques: Importar / Definir / `# 1)` `# 2)` `# 3)` |
| 35–40 | Demo del grupo + 1 frase de ODS |

Roles en el grupo (rotan cada lección): protoboard, código, sensores, prueba, anotar ciclos OK / paradas.

---

## Qué ya no se copia

| Libro | Qué hace él | Qué hace este |
|---|---|---|
| 4.º MECA | Casa, LOZ (dos sentidos, 18/19), puerta y elevador | Fábrica, DC un sentido, línea que produce o para |
| 5.º IA L7 | Dos modelos → LED y buzzer | Los mismos tipos de modelo **mueven el motor** |
| 5.º IA L8 | MPU IZQ/DER + ultra obstáculo + DC, todo el mismo día | El DC nace en L1; el molino/tacómetro es **L5**; L8 solo integra |

El molino **no va** en la L3 de 4.º (allí el segundo número es el pot) ni se mete dentro de la L8 de IA.

---

## Hardware de la línea (fijo en las 8)

Motor DC 3 V, **un sentido**, HIGH/LOW a tope. Sin PWM (en 3.3 V el DC se queda zumbando y no arranca). Sin puente H ni L298N.

| Pieza | GPIO / conexión |
|---|---|
| Base del transistor NPN | **18** (1 kΩ) |
| Motor (+) | **3V3** (nunca un GPIO) |
| Motor (−) | colector; emisor → GND |
| Diodo 1N4007 | ánodo al colector, cátodo a 3V3 |
| HC-SR04 TRIG / ECHO | **4** / **5** |
| MPU6050 SDA / SCL | **21** / **22** |
| LED de estado | **26** |
| Buzzer | **25** |
| Potenciómetro (pedido / demanda) | **34** |
| LDR | **35** |

`probar_motor.py`: GPIO 18 HIGH 4 s / LOW 2 s. Si no gira así, no pases a `main.py`.

---

## Progresión de hardware (un extra por clase)

| L | Se añade | Ya está |
|---|---|---|
| 1 | ESP32 + DC + transistor + diodo + LED | — |
| 2 | Servo + HC-SR04 | L1 |
| 3 | Potenciómetro | L1–2 |
| 4 | (ultra ya está: ahora mira la banda, no el servo) | L1–3 |
| 5 | Molino en el eje del DC; el ultra ahora mira **hélices** | L1–4 |
| 6 | MPU6050 | L1–5 |
| 7 | (MPU ya está: ahora es termostato / recta) | L1–6 |
| 8 | buzzer + todo junto | kit completo |

El motor puede llevar aspas desde L1 (se ve que “produce”). Contar palas es **solo L5**: ese día mueves el ultrasónico del frente de la banda al borde del molino.

---

## Progresión de ML (5.º: el modelo mueve la línea)

| L | ML (semilla) | Qué decide |
|---|---|---|
| 1 | Ninguno | Ciclo fijo: produce 4 s, para 2 s |
| 2 | Umbral 1D de distancia (presencia) | Ultra cerca → servo sigue; lejos → busca |
| 3 | Dos umbrales AND | Luz **y** pedido alto → produce |
| 4 | Clasificador 1D de distancia | Pieza cerca → un ciclo; lejos → espera |
| 5 | **Feature: hélices/s** (flanco + ventana 1 s) | Cadencia baja o 0 con motor ON → atasco / no produce |
| 6 | Umbral de inclinación / vibración (MPU) | Máquina ladeada o agitada → STOP |
| 7 | **Recta** `temp = m × inclinación + b` | 4 marcas de °C; predice 4 poses nuevas |
| 8 | 3 distancias → 3 tiempos de llenado | Envase → para + LED/buzzer; vacío → sigue; tope → regresa |

No meter visión/YOLO: 40 min con transistor y molino no dan.

---

## Las 8 lecciones

### 1. Movimiento de la línea: cinemática y el transistor
- **Teoría:** el GPIO no empuja el motor. El transistor conmuta 3V3. Tiempo ON = pieza que “salió”; tiempo OFF = la línea no gasta.
- **Práctica:** `probar_motor.py` y luego un ciclo fijo 4 s / 2 s. LED ON mientras produce.
- **ML:** no.
- **ODS:** 7 / 9 — ¿Cómo se mueve una línea con la menor energía y sin quemar el micro?
- **Salida:** consola “produce / espera”.

### 2. Seguidor de presencia: servo y ultrasónico
- **Teoría:** sensor de distancia → decisión → servo. Presencia = un rango de cm, no una cámara.
- **Práctica:** HC-SR04 + SG90. Sin persona: barre. Con persona (< 50 cm): mira izq/der y se queda en el eco más corto. LED ON mientras sigue.
- **ML:** clasificador 1D CERCA / LEJOS + regla de seguimiento.
- **ODS:** 9 — ¿Cómo apunta una máquina hacia quien está delante?

### 3. Pedido y entorno: dos condiciones para producir
- **Teoría:** una sola variable miente. Pedido alto de día ≠ producir a ciegas.
- **Práctica:** pot = pedido; LDR = luz. AND: claro **y** pedido ≥ umbral → produce un ciclo. Imprime los dos números.
- **ML:** regla AND; hábito de dato (como L5 de IA).
- **ODS:** 9 / 12 — ¿Qué hay que medir para no fabricar de más?
- **No:** molino ni ultrasónico. El segundo número es el pot.

### 4. Pieza en la banda: distancia y ciclo
- **Teoría:** entrada–proceso–salida. El humano no pulsa: la pieza dispara el ciclo.
- **Práctica:** HC-SR04 al frente. CERCA (p. ej. 5–20 cm) → un ciclo de N segundos; LEJOS → espera. Timeout 400 cm se ignora.
- **ML:** dos zonas CERCA / LEJOS.
- **ODS:** 9 / 12 — ¿Cómo actúa la línea sola, sin desperdiciar giros vacíos?

### 5. Midiendo la cadencia: tacómetro con molino y ultrasónico
- **Teoría:** el ultrasónico no da “RPM” de fábrica. Cada pala cercana es un pulso. Hélices en un segundo = cadencia de la línea. Hay que contar el **flanco** (lejos → cerca); si no, una pala se cuenta diez veces.
- **Práctica:** molino pequeño en el eje del DC, sensor a 5–10 cm del borde (no pegado: mínimo ~2 cm). Motor ON; consola `helices/s`. Umbral: pocas palas o 0 con motor ON → atasco, LED/buzzer, opcionalmente para. Molino **lento** (soplar o 3 V ya es suficiente); ping cada ~60 ms.
- **ML:** una feature nueva (frecuencia) + umbral de anomalía de cadencia. Aún no es clustering.
- **ODS:** 9 / 12 — ¿Cómo sabe la fábrica si está produciendo o solo zumbando?
- **Salida:** este es el sello del libro. No se adelanta a L8.

### 6. Salud de la máquina: vibración e inclinación
- **Teoría:** inclinación o golpe = fuerza que la línea no pidió. Parar es más barato que seguir.
- **Práctica:** MPU6050 plano = OK, el molino corre; ladeas o agitas = STOP + buzzer. La cadencia de L5 puede seguir en consola si el ultra sigue al molino.
- **ML:** umbral sobre `ax` / vibración (misma idea que el sismo de 4.º y el clustering de 5.º IA; hoy solo para no romper la máquina).
- **ODS:** 9 / 8 — ¿Cómo se mantiene estable la línea frente al uso?

### 7. El termostato aprende: regresión lineal
- **Teoría:** calibrar una escala. Cuatro marcas de °C que el estudiante sí conoce; la recta interpola las que no.
- **Práctica:** MPU6050 en el centro blanco del modelo K’NEX. 4 poses + °C a mano → `temp = m × ax + b`. Luego 4 poses nuevas: el modelo predice, el estudiante compara con la escala.
- **ML:** regresión lineal en la ESP32 (mínimos cuadrados, sin sklearn).
- **ODS:** 7 / 13 — ¿Cómo se calibra un termostato para no gastar de más?

### 8. Dosificador: el carrito llena y sigue
- **Teoría:** presencia + tamaño (distancia) → tiempo de dosificación. El recorrido no se detiene si no hay envase.
- **Práctica:** LOZ ida/vuelta por tiempo de tope. Ultra: 3 envases entrenados (3 s / 2 s / 1 s). Hay botella → para, LED y buzzer. Vacío → sigue y al tope regresa.
- **ML:** clasificador 1D de 3 centros (vecino más cercano).
- **ODS:** 9 / 12 — ¿Cómo llenas solo lo que hay, sin derramar ni viajar de más?

---

## Qué reutilizar (no reescribir de cero)

- `mpu6050.py` y `distancia_cm()` de 5.º IA. El DC + transistor de **este** libro no se copia de la L8 de IA (esa lección ahora usa servo).
- `mpu6050.py`, `distancia_cm()` con timeout, K-means a mano.
- Flanco + ventana 1 s del tacómetro (borrador en `TECNIBOT-10-MECA/Leccion 3/main.py`; **aquí es L5**, no L3 de 4.º).
- Fichas: Descripción, Electrónica (materiales + 2 pasos), Programación `# 1)` `# 2)` `# 3)`.
- Voz: INTRODUCCIÓN, PUNTO DE PARTIDA, CONCEPTOS con ejemplo de fábrica, DATO STEAM, ODS.
- Código ~80–110 líneas.

## Qué no hacer en este libro

- Motor LOZ (es 4.º MECA).
- Puente H / L298N / PWM al DC de 3 V.
- Ultrasónico en L3 (entra en L4 como distancia; en L5 como tacómetro).
- Molino como “viento de la casa” o como extra dentro de la L8 de IA.
- sklearn, YOLO, gráficas en PC.
- Dos ultrasónicos el mismo día.
- Tres mecanismos distintos en L8: un DC-molino + LED + buzzer basta.

## Orden de escritura (cuando pases de plan a material)

1. L1 ficha + transistor + `probar_motor` (ciclo HIGH/LOW del DC; no usar el servo de la L8 de IA).  
2. **L5 tacómetro** (sello del libro; molino + flanco).  
3. L4 ultra como pieza / distancia.  
4. L6 MPU STOP.  
5. L7 recta de demanda.  
6. L8 = L5+L6+L7 + K-means + contadores.  
7. L2 y L3 (luz y AND; rellenan con lo ya armado).

Así 5.º MECA es fábrica de verdad (el DC se ve desde L1), el molino tiene **su** clase, y L8 no inventa hardware nuevo: solo coordina lo que ya giraba y ya se medía.
