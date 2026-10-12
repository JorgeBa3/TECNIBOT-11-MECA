# LECCIÓN 4. Pieza en la banda: distancia y velocidad

## INTRODUCCIÓN

Hoy harás que **la banda de tu fábrica frene sola cuando una pieza se acerca al final**. El sensor ultrasónico mira la pieza que viaja sobre la banda: mientras está lejos, la banda va a toda velocidad; a medida que se acerca, el ESP32 le baja la velocidad al LOZ con PWM, y cuando la pieza llega al final, la banda se detiene. La LED avisa mientras la pieza está cerca. Nadie pulsa un botón: la distancia de la pieza decide la velocidad. Comprenderás cómo esta práctica contribuye al **ODS 9 (Industria, innovación e infraestructura)** y al **ODS 12 (Producción y consumo responsables)**, porque una banda que frena a tiempo no tira ni daña las piezas, y no gasta energía corriendo cuando ya no hay nada que mover.

## PUNTO DE PARTIDA

¿Cómo sabe una banda transportadora que debe ir más despacio para que la pieza no se caiga al llegar al final?

## CONCEPTOS IMPORTANTES

**Zonas de distancia:** El programa divide la banda en tres zonas usando dos números. Si la pieza está a `LEJOS` (40 cm) o más, o no hay pieza, la banda va al 100 %. Si está entre `PARADA` (9 cm) y `LEJOS`, la banda va más lento mientras más cerca esté y la LED se enciende para avisar que viene una pieza. Si llega a `PARADA` o menos, la banda se detiene y la LED sigue encendida hasta que quites la pieza.

**Regla de tres:** Para decidir la velocidad en la zona intermedia usamos una proporción: en `PARADA` la fuerza es `MINIMO` (lo más lento que sí mueve el LOZ) y en `LEJOS` es `MAXIMO` (1023). Cualquier distancia entre las dos da una fuerza proporcional. Así la banda frena de forma suave y no de golpe.

**Promedio de lecturas:** El ultrasónico a veces da lecturas que "tiemblan". Si usáramos una sola lectura, la velocidad de la banda cambiaría a saltos. Por eso la función `distancia_promedio()` toma 3 lecturas y usa su promedio.

**Sensor distinto de actuador:** El ultrasónico no mueve la banda; solo mide. El LOZ es el actuador que sí la mueve. El programa es el que conecta la lectura con la acción.

## DATO STEAM

¿Sabías que los elevadores hacen exactamente lo mismo que tu banda? Cuando un elevador se acerca al piso donde debe detenerse, reduce poco a poco su velocidad para quedar nivelado con el piso y que las personas no sientan un frenazo. Las bandas y los vehículos automáticos de las fábricas también tienen una "zona de frenado" antes de llegar a su destino.

Versión corta:  
¿Sabías que los elevadores frenan poco a poco antes de llegar a cada piso? Usan la misma idea que tu banda: mientras más cerca del destino, más lento, para detenerse con precisión y sin golpes.

## PRUEBA CORTA: Pieza en la banda

**Instrucciones:** Lee detenidamente cada pregunta y selecciona la opción que consideres correcta basándote en lo aprendido en la lección.

1. ¿Qué hace la banda cuando la pieza está a 40 cm o más, o cuando no hay pieza?  
a) Se detiene y enciende la LED.  
b) Va a toda velocidad (100 %).  
c) Gira en sentido contrario.

2. ¿Qué pasa con la velocidad de la banda a medida que la pieza se acerca al final?  
a) Aumenta para que la pieza llegue más rápido.  
b) Se mantiene igual todo el tiempo.  
c) Disminuye poco a poco, mientras más cerca más lento.

3. ¿Para qué se usa la regla de tres entre `PARADA` y `LEJOS`?  
a) Para calcular una velocidad proporcional a la distancia y que la banda frene de forma suave.  
b) Para contar cuántas piezas pasaron por la banda.  
c) Para decidir el color de la LED.

4. ¿Por qué el programa usa el promedio de 3 lecturas del ultrasónico?  
a) Porque el sensor solo funciona si se lee tres veces.  
b) Para que la velocidad no cambie a saltos cuando las lecturas tiemblan.  
c) Para que la banda gaste más energía.

5. ¿Qué pasa cuando la pieza llega a la distancia de `PARADA`?  
a) La banda se detiene y la LED queda encendida hasta que quites la pieza.  
b) La banda acelera al máximo.  
c) El programa se apaga por completo.

### Clave de evaluación (solo para el docente)

1. b) Va a toda velocidad (100 %).
2. c) Disminuye poco a poco, mientras más cerca más lento.
3. a) Para calcular una velocidad proporcional a la distancia y que la banda frene de forma suave.
4. b) Para que la velocidad no cambie a saltos cuando las lecturas tiemblan.
5. a) La banda se detiene y la LED queda encendida hasta que quites la pieza.
