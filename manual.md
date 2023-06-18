# Manual

1. Se importa el módulo `asciiFigures` utilizando la declaración `from asciiFigures import *`. Esto importa todas las funciones y variables definidas en el módulo `asciiFigures`.

2. Se importa el módulo `time`, que proporciona funciones relacionadas con el tiempo, como `sleep()` que se usa más adelante para introducir pausas en la ejecución del programa.

3. Se declara una variable `logoLines` y se asigna el valor de `logo.splitlines()`. Esto divide la cadena `logo` en líneas individuales y crea una lista de esas líneas. La variable `logo` no está definida en el código proporcionado, por lo que asumiremos que contiene algún tipo de arte ASCII para imprimirlo en pantalla.

4. Se inicia un bucle `for` que itera sobre cada línea en `logoLines`. En cada iteración, se imprime la línea y se utiliza `time.sleep(0.09)` para hacer una pausa de 0.09 segundos entre cada línea impresa. Esto crea un efecto de animación en la impresión del logo, mostrando cada línea con una breve pausa.

![image](https://github.com/johanP051/Adivinanzas/assets/64292875/f485af89-0834-46f8-a4e2-a6bb7d769f96)


5. Después de imprimir el logo, se muestra el mensaje "Ingresa la palabra correcta sin espacios".

6. Se define una lista de diccionarios llamada `adivinanzas`. Cada diccionario en esta lista representa una adivinanza y contiene tres elementos clave:
   - `"adivinanza"`: La adivinanza en sí, representada como una cadena de texto.
   - `"respuesta"`: Una lista de posibles respuestas correctas para la adivinanza.
   - `"pistas"`: Una lista de pistas que se mostrarán al jugador si falla en adivinar la respuesta.

![image](https://github.com/johanP051/Adivinanzas/assets/64292875/73bd5969-eb93-481e-81f2-18b02e1e4032)

7. Se declara una variable `contadorCorrectas` y se le asigna el valor inicial de 0. Esta variable se utiliza para realizar un seguimiento del número de respuestas correctas del jugador.

8. Se inicia un bucle `for` que itera sobre cada diccionario de adivinanza en la lista `adivinanzas`. En cada iteración, se imprime la adivinanza correspondiente utilizando `print(lista["adivinanza"])`.

9. Dentro del bucle `for`, se declara una variable `intentos_restantes` y se le asigna el valor de 3. Esta variable realiza un seguimiento del número de intentos que le quedan al jugador para adivinar la respuesta.

10. Se declara una variable `count` y se le asigna el valor inicial de 0. Esta variable se utiliza para rastrear el índice de la pista actual que se mostrará al jugador en caso de que falle en adivinar la respuesta.

![image](https://github.com/johanP051/Adivinanzas/assets/64292875/a501715a-412d-42cd-97b0-b9d09a9fadad)


11. Se inicia un bucle `while` que se ejecuta mientras `intentos_restantes` sea mayor que 0. Este bucle permite que el jugador realice múltiples intentos de adivinanza.

12. Dentro del bucle `while`, se le solicita al jugador que ingrese su respuesta utilizando `input("\nIntenta adivinar: ")`.

13. Si la respuesta ingresada por el jugador, convertida a minúsculas, coincide con alguna de las respuestas correctas en la lista `lista["respuesta"]`, se muestra el mensaje "\n¡Correcto! Has adivinado.", se incrementa el contador `contadorCorrectas` y se rompe el bucle `while` con la instrucción `break`.

14. Si la respuesta ingresada por el jugador no es correcta, se muestra el mensaje "\nLo siento, respuesta incorrecta.". Luego, se reduce en 1 el valor de `intentos_restantes`.

15. Si `intentos_restantes` es mayor que 0, se muestra una pista al jugador utilizando `print("\nPista:")`. La pista se obtiene de la lista `lista["pistas"]` utilizando el índice `count`. Luego, se divide la pista en líneas individuales y se imprime cada línea con una pausa de 0.09 segundos entre ellas, para crear un efecto de animación.

16. Si `intentos_restantes` es igual a 0, se muestra el mensaje "\nLo siento, has agotado tus intentos. La respuesta correcta era: [respuesta correcta]".

![image](https://github.com/johanP051/Adivinanzas/assets/64292875/bcd2952d-cab9-4c7a-a369-89bc3e4ab38a)


17. Después de que el bucle `while` termine, se calcula la cantidad total de adivinanzas en la variable `cantidadAdivinanzas` utilizando `len(adivinanzas)`.

18. Se imprime un mensaje que muestra la cantidad de respuestas correctas y la cantidad total de adivinanzas utilizando `f"\nTuviste {contadorCorrectas}/{cantidadAdivinanzas} respuestas correctas"`.

19. Si el contador `contadorCorrectas` es igual a la cantidad total de adivinanzas `cantidadAdivinanzas`, se imprime el mensaje "\n¡Enhorabuena, pudiste resolver todas las adivinanzas!\n".

20. Si el contador `contadorCorrectas` no es igual a la cantidad total de adivinanzas `cantidadAdivinanzas`, se imprime el mensaje "\nTe puede ir mejor la próxima vez, vuélvelo a intentar\n".

![image](https://github.com/johanP051/Adivinanzas/assets/64292875/9d6d68c7-4ee7-45c3-97ad-0bd9ba153a6f)
