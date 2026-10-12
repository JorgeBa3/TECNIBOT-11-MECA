# LECCIÓN 5. Seguidor de presencia: servo y ultrasónico

## INTRODUCCIÓN

Hoy aprenderás a **hacer que un servo mire hacia donde hay una persona**. El ultrasónico no “ve” la cara: mide distancia. Si alguien está a menos de 50 cm, hay presencia. El servo prueba un poco a la izquierda y a la derecha y se queda en el ángulo donde el eco es más corto: ahí está el cuerpo. Si la persona se aleja, vuelve a barrer. Comprenderás cómo esta práctica contribuye al **ODS 9: Industria, innovación e infraestructura**, porque cámaras de seguimiento, puertas automáticas y robots de servicio hacen lo mismo: un sensor de distancia y un actuador que apunta.

## PUNTO DE PARTIDA

¿Cómo puede una cabeza mecánica seguirte sin cámara ni visión?

## CONCEPTOS IMPORTANTES

**Presencia:** Es un rango de distancia, no un nombre. Entre 5 cm y `LIMITE` hay alguien; timeout 400 cm o muy lejos = vacío.

**Búsqueda:** Sin blanco, el servo barre de un lado al otro. Gasta movimiento, pero no se queda ciego en un solo ángulo.

**Seguimiento:** Con blanco, no barre todo: compara el ángulo actual con ± un paso y elige el más cercano. Es un clasificador mínimo: ¿dónde está más cerca?

**Pérdida:** Si el eco deja de entrar en el rango, se apaga el LED y vuelve la búsqueda. En un robot real eso es “no persigas un fantasma”.

## DATO STEAM

¿Sabías que muchos robots de almacén y cámaras PTZ no usan IA de video para el primer seguimiento? Un ultrasónico o un ToF dice “hay algo aquí” y un servo o un motor gira al eco más corto. Tu protoboard es esa cabeza: busca, sigue, y si te vas, busca otra vez.

Versión corta:  
¿Sabías que muchas cámaras y robots de almacén empiezan a seguirte sin inteligencia artificial de video? Un sensor de distancia detecta que hay algo cerca y un motor gira hacia el eco más corto, igual que tu servo.

## PRUEBA CORTA: Seguidor de presencia

**Instrucciones:** Lee detenidamente cada pregunta y selecciona la opción que consideres correcta basándote en lo aprendido en la lección.

1. ¿Cómo sabe el sistema que hay una persona frente a él?  
a) Reconoce su cara con una cámara.  
b) El ultrasónico mide una distancia dentro del rango de presencia (entre 5 cm y `LIMITE`).  
c) La persona presiona un botón para avisar que llegó.

2. ¿Qué hace el servo cuando no detecta a nadie?  
a) Barre de un lado al otro buscando.  
b) Se queda quieto en el centro.  
c) Se apaga por completo.

3. Cuando hay presencia, ¿cómo decide el servo hacia dónde mirar?  
a) Gira siempre hacia la derecha.  
b) Elige un ángulo al azar.  
c) Prueba un paso a la izquierda y a la derecha y se queda en el ángulo donde el eco es más corto.

4. ¿Qué pasa con la LED cuando la persona se aleja y sale del rango?  
a) Parpadea más rápido.  
b) Se apaga y el servo vuelve a buscar.  
c) Se queda encendida para siempre.

5. ¿Por qué esta práctica contribuye al ODS 9?  
a) Porque aplica la misma idea que usan cámaras de seguimiento, puertas automáticas y robots de servicio.  
b) Porque el servo genera energía mientras gira.  
c) Porque el ultrasónico funciona sin electricidad.

### Clave de evaluación (solo para el docente)

1. b) El ultrasónico mide una distancia dentro del rango de presencia (entre 5 cm y `LIMITE`).
2. a) Barre de un lado al otro buscando.
3. c) Prueba un paso a la izquierda y a la derecha y se queda en el ángulo donde el eco es más corto.
4. b) Se apaga y el servo vuelve a buscar.
5. a) Porque aplica la misma idea que usan cámaras de seguimiento, puertas automáticas y robots de servicio.
