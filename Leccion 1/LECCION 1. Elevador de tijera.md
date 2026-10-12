# LECCIÓN 1. Elevador de tijera: sube, espera y baja

## INTRODUCCIÓN

Hoy construirás el **elevador de carga de tu fábrica**: una plataforma de tijera que sube y baja sola. El motor LOZ enrolla un hilo en un carrete; al jalarlo, las barras cruzadas de la tijera se cierran y la plataforma sube. Cuando el motor gira al revés, suelta el hilo y la plataforma baja. Programarás el ESP32 para que el elevador siga siempre el mismo ciclo: sube, espera, baja y vuelve a esperar, sin que nadie presione un botón. Descubrirás que el ESP32 no alimenta el motor directamente: solo le da órdenes al driver, que es quien entrega la energía. Además, verás cómo esta práctica contribuye al **ODS 9 (Industria, innovación e infraestructura)** y al **ODS 8 (Trabajo decente y crecimiento económico)**, porque los elevadores de carga evitan que las personas levanten objetos pesados y hacen el trabajo en la fábrica más seguro.

## PUNTO DE PARTIDA

¿Cómo puede una máquina subir y bajar carga una y otra vez, sin que una persona tenga que cargarla ni controlarla?

## CONCEPTOS IMPORTANTES

**Mecanismo de tijera:** Son barras cruzadas en forma de X unidas por el centro. Cuando se jalan sus extremos para acercarlos, las X se cierran hacia los lados y se estiran hacia arriba; cuando se sueltan, bajan. En esta práctica el hilo del carrete jala la parte de abajo de la tijera y convierte el giro del motor en un movimiento de subida.

**Carrete (torno):** Es un cilindro que enrolla o desenrolla un hilo al girar. Está unido al eje del LOZ: si el motor gira hacia un lado, enrolla el hilo y la plataforma sube; si gira hacia el otro, lo desenrolla y la plataforma baja por su propio peso.

**Driver y sentido de giro:** Los pines del ESP32 solo entregan una señal pequeña que no alcanza para mover un motor. El driver recibe esa señal y deja pasar la energía de la batería hacia el LOZ. Tiene dos entradas: si enciendes IN1 (GPIO 19) el elevador sube; si enciendes IN2 (GPIO 18) baja; si apagas las dos, se detiene. Nunca se encienden las dos al mismo tiempo.

**Ciclo automático:** Es una secuencia que se repite sin fin dentro de un `while True`: sube `T_MOVER` segundos, espera `T_DESCANSO` segundos, baja `T_MOVER` segundos y espera otra vez. `T_MOVER` debe ser justo el tiempo que tarda en subir: si es muy largo, el motor sigue jalando cuando la tijera ya llegó arriba. Al presionar Ctrl+C, el programa apaga las dos entradas del driver y el elevador se detiene de forma segura.

## DATO STEAM

¿Sabías que las plataformas de tijera se usan en bodegas, fábricas y construcciones para subir personas y carga a varios metros de altura? Funcionan con el mismo principio que tu elevador: las barras cruzadas convierten un empuje o un jalón pequeño en una subida recta y estable. Gracias a ellas, los trabajadores no necesitan escaleras ni cargar objetos pesados, lo que reduce accidentes y lesiones.

Versión corta:  
¿Sabías que las plataformas de tijera de las bodegas y construcciones suben personas y carga a varios metros con barras cruzadas, igual que tu elevador? Así se evitan escaleras y cargas pesadas, y el trabajo es más seguro.

## PRUEBA CORTA: Elevador de tijera

**Instrucciones:** Lee detenidamente cada pregunta y selecciona la opción que consideres correcta basándote en lo aprendido en la lección.

1. ¿Qué pasa con la plataforma cuando el carrete enrolla el hilo y jala la parte de abajo de la tijera?  
a) La plataforma sube.  
b) La plataforma baja.  
c) La plataforma gira en círculos.

2. ¿Por qué el motor LOZ se conecta a un driver y no directamente a un pin del ESP32?  
a) Porque el driver hace que el motor gire más lento.  
b) Porque los pines del ESP32 solo dan una señal pequeña; el driver es quien entrega la energía al motor.  
c) Porque el ESP32 no puede enviar ninguna señal a otros componentes.

3. En el driver, ¿qué pasa si enciendes IN2 y apagas IN1?  
a) El elevador sube.  
b) El elevador se detiene.  
c) El elevador baja.

4. ¿Qué podría pasar si `T_MOVER` es mucho más largo que el tiempo que tarda la plataforma en subir?  
a) El elevador subiría más rápido.  
b) El motor seguiría jalando el hilo cuando la tijera ya llegó arriba, forzando el mecanismo.  
c) No pasaría nada, el motor se apaga solo.

5. ¿Por qué esta práctica contribuye al ODS 8 y al ODS 9?  
a) Porque los elevadores de carga evitan que las personas levanten objetos pesados y hacen el trabajo más seguro.  
b) Porque el elevador genera energía al bajar.  
c) Porque el mecanismo de tijera está hecho con materiales reciclados.

### Clave de evaluación (solo para el docente)

1. a) La plataforma sube.
2. b) Porque los pines del ESP32 solo dan una señal pequeña; el driver es quien entrega la energía al motor.
3. c) El elevador baja.
4. b) El motor seguiría jalando el hilo cuando la tijera ya llegó arriba, forzando el mecanismo.
5. a) Porque los elevadores de carga evitan que las personas levanten objetos pesados y hacen el trabajo más seguro.
