# LECCIÓN 2. Línea de producción: la perilla decide la velocidad

## INTRODUCCIÓN

Hoy harás que **tu línea de producción cambie de velocidad con una perilla**. En la lección 1 el motor LOZ siempre giraba a toda fuerza; hoy conectarás un potenciómetro de 10K y el ESP32 leerá su posición para decidir qué tan rápido produce la línea. Aprenderás a usar **PWM**, la técnica con la que el ESP32 regula la velocidad de un motor prendiéndolo y apagándolo muy rápido. Además, verás cómo esta práctica contribuye al **ODS 9 (Industria, innovación e infraestructura)** y al **ODS 12 (Producción y consumo responsables)**, porque una fábrica que ajusta su velocidad a lo que necesita no gasta energía ni materiales de más.

## PUNTO DE PARTIDA

Si una fábrica no necesita producir tanto hoy, ¿por qué dejaría sus máquinas funcionando a toda velocidad?

## CONCEPTOS IMPORTANTES

**Potenciómetro:** Es una resistencia variable con una perilla. Al girarla, cambia el voltaje que llega al pin del medio. En esta práctica está conectado al GPIO 34 y el ESP32 lo lee como un número entre 0 y 4095: 0 es la perilla al mínimo y 4095 al máximo.

**PWM (Modulación por Ancho de Pulso):** El ESP32 no puede bajar el voltaje que llega al motor, pero sí puede prenderlo y apagarlo 1000 veces por segundo. Si lo deja prendido más tiempo en cada ciclo (`duty` alto), el motor va más rápido; si lo deja prendido menos tiempo, va más lento. En esta práctica el `duty` va de 0 a 1023, por eso convertimos la lectura de la perilla con `lectura * 1023 // 4095`.

**Fuerza mínima:** Con muy poca fuerza, el LOZ zumba pero no alcanza a girar. Eso gasta energía sin producir nada. Por eso el programa usa `MINIMO = 350`: si la perilla da menos que eso, la línea se detiene. Cada motor es distinto, así que puedes ajustar ese número al tuyo.

**Un solo sentido:** En una línea de producción las piezas avanzan siempre hacia adelante. Por eso IN2 (GPIO 18) queda siempre apagado y solo IN1 (GPIO 19) recibe el PWM.

## DATO STEAM

¿Sabías que en las fábricas los ventiladores y bombas grandes se controlan con **variadores de velocidad**, que usan la misma idea del PWM? En este tipo de máquinas, bajar la velocidad a la mitad puede reducir el consumo de energía a cerca de una octava parte. Por eso ajustar la velocidad a lo que realmente se necesita es una de las formas más efectivas de ahorrar energía en la industria.

Versión corta:  
¿Sabías que en ventiladores y bombas industriales, bajar la velocidad a la mitad puede reducir el consumo de energía a cerca de una octava parte? Los variadores de velocidad usan la misma idea del PWM que aplicas hoy con tu perilla.

## PRUEBA CORTA: Línea de producción con perilla

**Instrucciones:** Lee detenidamente cada pregunta y selecciona la opción que consideres correcta basándote en lo aprendido en la lección.

1. ¿Qué rango de valores entrega el potenciómetro cuando el ESP32 lo lee en el GPIO 34?  
a) De 0 a 100.  
b) De 0 a 4095.  
c) De 0 a 1023.

2. ¿Cómo regula el ESP32 la velocidad del motor usando PWM?  
a) Prendiendo y apagando el motor muy rápido; mientras más tiempo prendido en cada ciclo, más rápido gira.  
b) Cambiando el sentido de giro del motor cada segundo.  
c) Calentando el motor para que gire con más facilidad.

3. ¿Para qué sirve el valor `MINIMO = 350` en el programa?  
a) Para que el motor siempre gire a la máxima velocidad.  
b) Para contar cuántas piezas produce la línea.  
c) Para detener la línea cuando la fuerza es tan baja que el motor solo zumbaría sin girar.

4. ¿Por qué IN2 (GPIO 18) permanece siempre apagado en esta práctica?  
a) Porque la línea de producción avanza en un solo sentido.  
b) Porque ese pin está dañado en el ESP32.  
c) Porque IN2 es el que lee el potenciómetro.

5. Según el Dato STEAM, ¿qué pasa con el consumo de un ventilador o bomba industrial si se baja su velocidad a la mitad?  
a) Consume el doble de energía.  
b) Puede consumir cerca de una octava parte de la energía.  
c) El consumo no cambia.

### Clave de evaluación (solo para el docente)

1. b) De 0 a 4095.
2. a) Prendiendo y apagando el motor muy rápido; mientras más tiempo prendido en cada ciclo, más rápido gira.
3. c) Para detener la línea cuando la fuerza es tan baja que el motor solo zumbaría sin girar.
4. a) Porque la línea de producción avanza en un solo sentido.
5. b) Puede consumir cerca de una octava parte de la energía.
