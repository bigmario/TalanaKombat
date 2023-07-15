# Talana Kombat JRPG
Talana Kombat es un juego donde 2 personajes se enfrentan hasta la muerte.<br> 
Cada personaje tiene 2 golpes especiales que se ejecutan con una combinación de movimientos + 1 botón de golpe.

Los botones que se usan son

(W)Arriba<br>
(S)Abajo<br> 
(A)Izquierda<br> 
(D)Derecha<br>
(P)Puño<br> 
(K)Patada<br>

Movimientos de los personajes

Tonyn Stallone:
- Puño: quita 1 de energía
- Patada: quita 1 de energía
- Taladoken:  DSD + P, quita 3 de Energía
- Remuyuken:  SD + K, quita 2 de Energía

Arnaldor Shuatseneguer
- Puño: quita 1 de energía
- Patada: quita 1 de energía
- Remuyuken:  SA + K, quita 3 de Energía
- Taladoken:  ASA + P,  quita 2 de Energía


Reglas:

1. Parte atacando el jugador que envió una combinación menor de botones (movimiento + golpes), en caso de empate, parte el con menos movimientos, si empatan de nuevo, inicia el con menos golpes, si hay empate de nuevo, inicia el player 1

2. La secuencia completa del combate de cada jugador se entrega de una vez (consolidada
en un json)

3. Cada personaje tiene 6 Puntos de energía
    - Un personaje muere cuando su energía llega a 0 y de inmediato finaliza la pelea
    - Tonyn es el player 1, siempre ataca hacia la derecha (y no cambia de lado)
    - Arnaldor es el player 2, siempre ataca hacia la izquierda (y no cambia de lado)
    - Los personajes se atacan uno a la vez estilo JRPG, por turnos hasta que uno es derrotado, los golpes no pueden ser bloqueados, se asume que siempre son efectivos.

4. Los datos llegan como un json con botones de movimiento y golpe que se correlacionan para cada jugada.

5. Los movimientos pueden ser un string de largo máximo 5 (puede ser vacío)

6. Los golpes pueden ser un solo botón máximo (puede ser vacío).
7. Se asume que el botón de golpe es justo después de la secuencia de movimiento, es decir, AADSD + P es un Taladoken (antes se movió para atrás 2 veces); DSDAA + P son movimientos más un puño


#### Ejemplo de JSON de pelea:
```jsonc
{

  "player1": {

    "movimientos": [ "D",  "DSD",  "S",  "DSD",  "SD"],
    "golpes": [ "K",  "P", "",  "K", "P"]
  },
  "player2": {

    "movimientos": [ "SA", "SA", "SA", "ASA", "SA"],
    "golpes": [ "K", "", "K","P", "P"]
  }
}
```

el resultado es el siguiente
- Tonyn avanza y da una patada
- Arnaldor conecta un Remuyuken
- Tonyn usa un Taladoken
- Arnaldor se mueve
- Tonyn le da un puñetazo a Arnaldor
- Arnaldor conecta un Remuyuken
- Arnardol Gana la pelea.

#### Otros ejemplos de JSON de pelea:
```jsonc
#Gana Tonyn
{

    "player1": {

        "movimientos": ["SDD", "DSD", "SA", "DSD"],
        "golpes": ["K", "P", "K", "P"],
    },
    "player2": {

        "movimientos": ["DSD", "WSAW", "ASA", "", "ASA", "SA"],
        "golpes": ["P", "K", "K", "K", "P", "K"],
    },
}
```

```jsonc
#Gana Arnaldor
{

    "player1": {

         "movimientos": ["DSD", "S"],
        "golpes": ["P", ""],
    },
    "player2": {

        "movimientos": ["", "ASA", "DA", "AAA", "", "SA"],
        "golpes": ["P", "", "P", "K", "K", "K"],
    },
}
```

## Para este desafío: Desarrollar una solución que relate la pelea e informe el resultado final.

### Solución:
El código resuelve un problema relacionado con un juego llamado "Talana Kombat", que simula una pelea entre dos personajes, Tonyn Stallone y Arnaldor Shuatseneguer, en el estilo de un juego de rol japonés (JRPG). El objetivo es desarrollar una solución en Python que narre la pelea y determine al ganador siguiendo ciertas reglas establecidas.

El código se divide en varias funciones, cada una con una responsabilidad específica:

1. La función `ejecutar_golpe` recibe como parámetros el personaje, el movimiento y el golpe. Su objetivo es determinar qué acción realiza el personaje y devolver la narración correspondiente junto con la energía del golpe. La función contiene lógica condicional para cada personaje y su conjunto de movimientos y golpes. Si se encuentra una combinación válida de movimiento y golpe para un personaje específico, se genera una narración adecuada y se asigna la energía correspondiente al golpe ejecutado. Además, también se tiene en cuenta la posibilidad de movimientos adicionales como "Arriba", "Abajo", "Izquierda" y "Derecha", registrando la acción de movimiento correspondiente.

2. La función `determinar_ganador` recibe las energías de ambos personajes y se encarga de determinar al ganador según las reglas establecidas. Si la energía de Tonyn Stallone (personaje 1) es menor o igual a cero, se declara a Arnaldor Shuatseneguer como ganador. Por otro lado, si la energía de Arnaldor Shuatseneguer (personaje 2) es menor o igual a cero, se declara a Tonyn Stallone como ganador. Si ninguna de estas condiciones se cumple, se considera que la pelea termina en empate.

3. La función principal `narrar_pelea` recibe un JSON que contiene las acciones de ambos personajes. Su propósito es narrar la pelea entre los personajes basándose en las acciones proporcionadas. La función comienza inicializando variables como las energías de ambos personajes y los nombres de los personajes involucrados en la pelea. Luego, itera sobre el número máximo de turnos, que se determina tomando la longitud máxima de las listas de movimientos de ambos personajes. Esto garantiza que ambos personajes tengan la misma cantidad de turnos narrados. Dentro del bucle, se obtienen los movimientos y golpes correspondientes de cada personaje en el turno actual y se llama a la función `ejecutar_golpe` para obtener la narración específica y la energía del golpe. Luego, se actualizan las energías de los personajes según los golpes ejecutados. La narración se va acumulando en una variable de texto. Al finalizar el bucle, se determina al ganador utilizando la función `determinar_ganador` y se agrega esa información a la narración.

Finalmente, se proporcionan tres ejemplos de peleas en formato JSON. Cada pelea contiene las acciones de ambos personajes, incluyendo movimientos y golpes. Se utiliza la función `narrar_pelea` para narrar cada pelea y el resultado se imprime por pantalla.

En resumen, el código implementa un algoritmo que permite simular peleas entre personajes en el juego "Talana Kombat". Proporciona una narración de la pelea y determina al ganador basándose en las acciones y reglas establecidas. El código se organiza en funciones para modularizar la lógica y facilitar la comprensión y el mantenimiento del programa.

### Ejecución de la solución
```bash
# Directamente con el intérprete Python
$ python3 main.py

# Mediante Docker (haciendo build de los archivos locales)
$ docker build -t talanakombat .
$ docker run talanakombat

# Mediante Docker (desde DockerHub)
$ docker run bigmario/talanakombat_script
```

### Preguntas Generales
1. Supongamos que en un repositorio GIT hiciste un commit y olvidaste un archivo. Explica cómo se soluciona si hiciste push, y cómo si aún no hiciste.<br> 
De ser posible, que quede solo un commit con los cambios.<br>
    Si ya hice push: 
    - Añado el archivo olvidado con ```git add <nombre_del_archivo>``` para agregar el archivo olvidado a staging. Luego, utilizaría el comando ```git commit --amend``` para crear un nuevo commit que incluya los cambios del archivo olvidado junto con los cambios del commit anterior.
    - Edito el mensaje del commit con ```git commit --amend``` para dejar constancia de la situación en el mensaje del commit. 
    - Dado que ya he realizado push anteriormente, necesitare hacer un push forzado para sobrescribir el commit anterior en el repositorio remoto con ```git push --force origin <nombre_de_la_rama>```<br><br>
    
    En caso de no haber hecho push cambiaria l comando del último paso por ```git push --force-with-lease origin <nombre_de_la_rama>``` porque si alguien más ha realizado cambios en la misma rama remota desde que hice el último pull, Git rechazará el push. En ese caso, puedes utilizar el comando ```--force-with-lease``` sobrescribirá el commit anterior en el repositorio remoto.
2. Si has trabajado con control de versiones ¿Cuáles han sido los flujos con los que has trabajado?<br>
Mi experiencia ha sido con Gitflow

3. ¿Cuál ha sido la situación más compleja que has tenido con esto?: Típicamente una situación compleja  que surge al trabajar con el enfoque de Gitflow es la resolución de conflictos durante la fusión de ramas.
En tales situaciones, es fundamental colaborar estrechamente con el desarrollador (Yo?) que ha trabajado en el feature que genera el conflicto para comprender su implementación y resolver todo de manera adecuada. También es importante asegurarse de que las pruebas sean realizadas exhaustivamente después de la resolución para garantizar que el código fusionado funcione correctamente y no introduzca errores en la rama de lanzamiento.

4. ¿Qué experiencia has tenido con los microservicios?: Como desarrollador backend, estuve involucrado en el análisis, desarrollo e implementación de un Data Warehouse utilizando microservicios. Una de las tareas clave en este proyecto fue el proceso de Extracción, Transformación y Carga (ETL) de datos desde API's y una Base de Datos MongoDB en simultáneo.

    Para lograr esto, utilicé Python y Celery para implementar tareas programadas. Python es un lenguaje versátil que me permitió conectarme a las API's y a la Base de Datos MongoDB para extraer los datos necesarios. Celery fue utilizado como un sistema de colas de tareas distribuido, lo que me permitió gestionar de manera eficiente la ejecución de las tareas de ETL.

    Además, utilizamos RabbitMQ como nuestro servicio de Broker para establecer la comunicación entre los diferentes microservicios involucrados en el proceso de ETL. RabbitMQ nos brindó la capacidad de enviar y recibir mensajes entre los distintos componentes del sistema, asegurando una comunicación confiable y escalable.

5. ¿Cuál es tu servicio favorito de GCP o AWS? ¿Por qué?: Mi experiencia ha sido primordialmente con AWS y me gusta mucho EC2 y la libertad que me da de armar la arquitectura de mis servicios de la manera que yo quiera utilizando VPC's, Internet Gateways, ACL's, etc.





