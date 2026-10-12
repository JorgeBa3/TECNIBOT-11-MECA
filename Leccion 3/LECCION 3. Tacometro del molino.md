# LECCIÓN 3. Tacómetro del molino: perilla y vueltas

## INTRODUCCIÓN

Hoy aprenderás a **medir qué tan rápido produce tu máquina**. En la lección 2 la perilla (potenciómetro) decidía la velocidad del LOZ, pero solo lo veías "a ojo". Hoy el ultrasónico mira el molino que gira en el eje del motor: cada vez que un aspa pasa frente a él, el eco se vuelve corto de golpe. Si cuentas esos saltos durante unos segundos, sabes cuántas vueltas por segundo da la máquina. Eso es un **tacómetro**, el mismo instrumento que marca las revoluciones en el tablero de un carro. Comprenderás cómo esta práctica contribuye al **ODS 9: Industria, innovación e infraestructura** y al **ODS 12: Producción y consumo responsables**, porque una fábrica que mide su propio ritmo sabe si produce lo que debe o si está gastando energía de más.

## PUNTO DE PARTIDA

Si giras la perilla al doble, ¿el molino da el doble de vueltas? ¿Cómo podrías comprobarlo con números y no solo mirando?

## CONCEPTOS IMPORTANTES

**PWM (control de velocidad):** El ESP32 no le baja el voltaje al LOZ; lo prende y apaga 1000 veces por segundo. Si está prendido más tiempo del ciclo (`duty` alto), el motor va más rápido. La perilla da un número de 0 a 4095 y lo convertimos a 0–1023 para el `duty`.

**Fuerza mínima:** Con muy poca fuerza el LOZ zumba pero no gira. Por eso existe `MINIMO`: debajo de ese valor el programa prefiere apagarlo. Cada motor es distinto; encuentra el tuyo.

**Flanco:** No contamos "cuántas veces el aspa está cerca", porque mientras el aspa pasa el ultra la ve varias lecturas seguidas. Contamos el **cambio** de LEJOS a CERCA: eso es un flanco. Un flanco = una pasada de aspa.

**Histéresis:** Para decir que el aspa "ya se fue" pedimos que el eco pase de `UMBRAL + HISTERESIS`, no solo de `UMBRAL`. Así, si la distancia tiembla justo en el borde, no contamos dos pasadas donde solo hubo una.

**Ventana de tiempo:** Contamos pasadas durante `VENTANA` (2 s) y luego dividimos: vueltas/s = pasadas ÷ aspas ÷ segundos. Multiplicado por 60 da **rpm** (revoluciones por minuto).

**Límite del sensor:** El ultrasónico hace unas 25 lecturas por segundo. Si el aspa pasa más rápido de lo que el sensor alcanza a mirar, se la salta y el tacómetro marca menos de lo real. Por eso conviene un molino con **1 o 2 aspas** anchas y planas, y no uno con muchas aspas delgadas.

## DATO STEAM

¿Sabías que los tacómetros de verdad usan la misma idea? Un sensor óptico o magnético ve pasar una marca en el eje y el aparato cuenta pulsos por segundo. Tu molino, el HC-SR04 y una resta de tiempos hacen exactamente lo mismo.

Versión corta:  
¿Sabías que el tacómetro de un carro cuenta pulsos, igual que tu molino? Un sensor ve pasar una marca en el eje y el aparato calcula las vueltas por segundo; tú lo haces con un ultrasónico y un reloj.

## DESAFÍOS

1. Llena una tabla: perilla al 40 %, 55 %, 70 %, 85 % y 100 %, y anota las vueltas/s de cada una. ¿Crecen parejo o no?
2. Cambia `ASPAS` y el molino (de 1 a 2 aspas). ¿Las vueltas/s siguen iguales? Deberían: cambian las pasadas, no las vueltas.
3. Pon la perilla al máximo y frena el molino suavemente con un dedo. ¿Qué pasa con las rpm? ¿Cómo usaría esto una fábrica para saber que una máquina se atascó?

## PRUEBA CORTA: Tacómetro del molino

**Instrucciones:** Lee detenidamente cada pregunta y selecciona la opción que consideres correcta basándote en lo aprendido en la lección.

1. ¿Qué es un tacómetro?  
a) Un instrumento que mide la temperatura del motor.  
b) Un instrumento que mide qué tan rápido gira algo (vueltas por segundo o rpm).  
c) Un sensor que detecta si hay personas cerca de la máquina.

2. ¿Por qué el programa cuenta el **flanco** (el cambio de LEJOS a CERCA) y no cada lectura en la que el aspa está cerca?  
a) Porque mientras el aspa pasa, el sensor la ve varias lecturas seguidas y se contaría varias veces.  
b) Porque el sensor solo funciona cuando el aspa está lejos.  
c) Porque así el motor gira más rápido.

3. ¿Para qué sirve la **histéresis** en el tacómetro?  
a) Para que el motor gire en los dos sentidos.  
b) Para aumentar la velocidad del ultrasónico.  
c) Para no contar dos pasadas cuando la distancia tiembla justo en el borde del umbral.

4. Si en una ventana de 2 segundos el ultra cuenta 6 pasadas y el molino tiene 1 aspa, ¿cuántas vueltas por segundo da?  
a) 3 vueltas/s.  
b) 6 vueltas/s.  
c) 12 vueltas/s.

5. ¿Por qué conviene usar un molino de 1 o 2 aspas anchas y no uno de muchas aspas delgadas?  
a) Porque las aspas delgadas pesan más.  
b) Porque el ultrasónico hace unas 25 lecturas por segundo y, si las aspas pasan muy rápido, se las salta.  
c) Porque el potenciómetro solo funciona con molinos pequeños.

### Clave de evaluación (solo para el docente)

1. b) Un instrumento que mide qué tan rápido gira algo (vueltas por segundo o rpm).
2. a) Porque mientras el aspa pasa, el sensor la ve varias lecturas seguidas y se contaría varias veces.
3. c) Para no contar dos pasadas cuando la distancia tiembla justo en el borde del umbral.
4. a) 3 vueltas/s.
5. b) Porque el ultrasónico hace unas 25 lecturas por segundo y, si las aspas pasan muy rápido, se las salta.
