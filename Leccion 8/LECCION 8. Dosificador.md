# LECCIÓN 8. Dosificador: el carrito llena y sigue

## INTRODUCCIÓN

Hoy **vas a convertir el riel en un dosificador**. El motor LOZ mueve el carrito de un lado al otro. Un ultrasónico mira si hay envase. Tres medidas que tú entrenas (grande, mediano, chico) se vuelven tres tiempos de parada arriba: más cerca, más rato vaciando. LED y buzzer avisan que está llenando. Si no hay botella, el carrito no se detiene: llega al tope, regresa y vuelve a preguntar. No es un modelo nuevo de fábrica completa: es clasificar una distancia y dosificar tiempo. Comprenderás cómo esta práctica contribuye al **ODS 9: Industria, innovación e infraestructura** y al **ODS 12: Producción y consumo responsables**, porque llenar solo cuando hay envase, y solo el tiempo que pide el tamaño, evita derrames y ciclos vacíos.

## PUNTO DE PARTIDA

¿Cómo llena solo el envase que hay, sin quedarse parado si la estación está vacía?

## CONCEPTOS IMPORTANTES

**Dosificación:** Es entregar una cantidad (aquí, segundos de parada) según lo que mediste. El ultra no “sabe” litros: tú entrenas tres distancias y cada una manda un tiempo.

**Recorrido y tope:** El LOZ no tiene encoder. El tope es un tiempo de giro (`TIEMPO_TOPE`). Al cumplirse, inviertes el sentido. En una línea real habría un final de carrera; aquí el reloj hace esa función.

**Presencia:** Si el eco está lejos o en timeout, no hay envase: sigue viajando. Si coincide con un centro entrenado, llena una vez y no vuelve a llenar hasta que el envase se aleje.

**Indicación:** LED y buzzer no mueven líquido; dicen “estoy vaciando” para que el grupo vea el estado.

## DATO STEAM

¿Sabías que una llenadora de bebidas no corre la cinta a ciegas? Un sensor confirma que hay botella y el tiempo de válvula cambia con el formato (330 ml vs 1 L). Tu K’NEX hace esa lógica: tres tamaños, un carrito que no para si no hay envase, y una alarma visual y sonora mientras dosifica.

Versión corta:  
¿Sabías que las llenadoras de bebidas cambian el tiempo de llenado según el tamaño de la botella? Un sensor confirma que hay envase y la máquina dosifica solo lo necesario, igual que tu carrito con sus tres tamaños entrenados.

## PRUEBA CORTA: Dosificador

**Instrucciones:** Lee detenidamente cada pregunta y selecciona la opción que consideres correcta basándote en lo aprendido en la lección.

1. ¿Qué significa "dosificar" en esta práctica?  
a) Mover el carrito lo más rápido posible.  
b) Entregar una cantidad (segundos de llenado) según el envase que se midió.  
c) Apagar el sensor cuando no hay envase.

2. ¿Cómo sabe el carrito que llegó al final del riel (tope)?  
a) Por un tiempo de giro (`TIEMPO_TOPE`): al cumplirse, invierte el sentido.  
b) Porque el ultrasónico mide la pared del final.  
c) Porque el buzzer suena al chocar.

3. ¿Qué hace el carrito si no hay envase frente al ultrasónico?  
a) Se detiene y espera hasta que alguien ponga uno.  
b) Enciende el buzzer sin parar.  
c) Sigue viajando: llega al tope, regresa y vuelve a preguntar.

4. En el entrenamiento, ¿qué relación hay entre el tamaño del envase y el tiempo de llenado?  
a) Todos los envases se llenan durante el mismo tiempo.  
b) El envase GRANDE (más cerca del sensor) recibe más tiempo: 3 s; el MEDIANO 2 s y el CHICO 1 s.  
c) El envase CHICO recibe más tiempo porque está más lejos.

5. ¿Qué técnica usa el programa para encontrar el centro de cada uno de los tres envases entrenados?  
a) K-means con 3 centros.  
b) Regresión lineal.  
c) Un solo umbral de distancia.

### Clave de evaluación (solo para el docente)

1. b) Entregar una cantidad (segundos de llenado) según el envase que se midió.
2. a) Por un tiempo de giro (`TIEMPO_TOPE`): al cumplirse, invierte el sentido.
3. c) Sigue viajando: llega al tope, regresa y vuelve a preguntar.
4. b) El envase GRANDE (más cerca del sensor) recibe más tiempo: 3 s; el MEDIANO 2 s y el CHICO 1 s.
5. a) K-means con 3 centros.
