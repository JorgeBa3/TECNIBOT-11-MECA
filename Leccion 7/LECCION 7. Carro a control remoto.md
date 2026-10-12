# LECCIÓN 7. Carro a control remoto: el control aprende tus gestos

## INTRODUCCIÓN

Hoy construirás un **carro a control remoto que se maneja inclinando un control**. El control es un sensor MPU6050 que mide hacia dónde lo inclinas. Primero lo entrenarás: le mostrarás cómo se ve "izquierda", "derecha" y "horizontal", y el ESP32 usará **K-means** para encontrar el centro de cada gesto. Después, cada vez que inclines el control, el ESP32 buscará el centro más cercano y moverá el LOZ: izquierda = adelante, derecha = atrás, horizontal = parado. Comprenderás cómo esta práctica contribuye al **ODS 9 (Industria, innovación e infraestructura)**, porque los vehículos y máquinas que se controlan con gestos permiten manejar equipos de forma más natural y accesible, incluso para personas que no pueden usar botones o palancas.

## PUNTO DE PARTIDA

¿Cómo puede una máquina aprender a reconocer tus gestos para obedecerte sin botones?

## CONCEPTOS IMPORTANTES

**MPU6050 (acelerómetro):** Es un sensor que mide aceleración en tres ejes. Cuando el control está quieto, la única aceleración que mide es la gravedad, y con ella el programa calcula dos ángulos de inclinación: `ang_x` y `ang_y`. Cada lectura es un punto con dos números, por ejemplo (−35, 4). El sensor se conecta por I2C: SCL al GPIO 22 y SDA al GPIO 21.

**Entrenamiento:** Antes de manejar, el estudiante inclina el control en cada pose (IZQUIERDA, DERECHA y HORIZONTAL) y pulsa Enter. El programa toma 10 lecturas de cada pose. Moverlo un poquito mientras mide ayuda a que el modelo aprenda que un gesto no siempre es exactamente igual.

**K-means de 3 centros:** Es un algoritmo que agrupa puntos parecidos. Empieza con 3 centros, asigna cada lectura al centro más cercano y mueve cada centro al promedio de sus puntos; repite esto 10 veces. Luego cada centro recibe el nombre de la pose que más lecturas tuvo en él (votación por mayoría). Si dos poses quedan en el mismo centro, el programa avisa para que vuelvas a entrenar inclinando más.

**Confirmación de la orden:** Para cambiar lo que hace el carro, el programa pide que la misma pose aparezca **3 lecturas seguidas** (`N_SEGUIR`). Así, un temblor de la mano no hace que el carro cambie de sentido por error. Además, antes de cambiar de sentido el motor se detiene un instante para no forzar el LOZ.

## DATO STEAM

¿Sabías que uno de los primeros controles de videojuegos que se manejaban inclinándolos fue el Wii Remote, lanzado en 2006? Tenía un acelerómetro, como tu MPU6050, que detectaba hacia dónde lo movías. Hoy la misma idea se usa en sillas de ruedas que se controlan con movimientos de la cabeza, en drones que se manejan con gestos y en brazos robóticos de fábrica que imitan los movimientos de un operador.

Versión corta:  
¿Sabías que el Wii Remote, lanzado en 2006, usaba un acelerómetro como tu MPU6050 para saber hacia dónde lo movías? Hoy esa idea permite manejar sillas de ruedas, drones y robots con simples gestos.

## PRUEBA CORTA: Carro a control remoto

**Instrucciones:** Lee detenidamente cada pregunta y selecciona la opción que consideres correcta basándote en lo aprendido en la lección.

1. ¿Qué mide el MPU6050 que usamos como control del carro?  
a) La distancia a los obstáculos frente al carro.  
b) La aceleración, con la que el programa calcula hacia dónde está inclinado el control.  
c) La temperatura del motor LOZ.

2. ¿Para qué sirve el entrenamiento al inicio del programa?  
a) Para que el ESP32 aprenda cómo se ven los gestos IZQUIERDA, DERECHA y HORIZONTAL a partir de lecturas reales.  
b) Para cargar la batería del carro.  
c) Para que el motor gire a toda velocidad desde el principio.

3. ¿Qué hace el algoritmo K-means en esta práctica?  
a) Mide la velocidad del carro en km/h.  
b) Enciende el motor cada 10 segundos.  
c) Agrupa las lecturas parecidas y encuentra un centro para cada gesto.

4. ¿Qué movimiento hace el carro con cada gesto?  
a) Izquierda = atrás, derecha = adelante, horizontal = gira.  
b) Izquierda = adelante, derecha = atrás, horizontal = parado.  
c) Cualquier gesto hace que el carro avance.

5. ¿Por qué el programa pide que la misma pose aparezca 3 lecturas seguidas antes de cambiar de orden?  
a) Para que un temblor de la mano no cambie el sentido del carro por error.  
b) Para que el carro vaya tres veces más rápido.  
c) Porque el MPU6050 solo funciona cada tres lecturas.

### Clave de evaluación (solo para el docente)

1. b) La aceleración, con la que el programa calcula hacia dónde está inclinado el control.
2. a) Para que el ESP32 aprenda cómo se ven los gestos IZQUIERDA, DERECHA y HORIZONTAL a partir de lecturas reales.
3. c) Agrupa las lecturas parecidas y encuentra un centro para cada gesto.
4. b) Izquierda = adelante, derecha = atrás, horizontal = parado.
5. a) Para que un temblor de la mano no cambie el sentido del carro por error.
