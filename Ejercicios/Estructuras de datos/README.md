# Funciones y estructuras de datos

  El problema de esta semana presenta un reto, puesto que usted debe de crear el codigo que presente el siguiente patrón, o mejor dicho juego, al que será llamado
**_Cartas Magicas_**, donde tiene que encontrar un patrón de **"aleatoriedad"**, y replicarlo.

###  **Reglas del juego**:

  - Leerá un número máximo, es decir, una cota superior.
  - Generará conjuntos ¿"aleatorios"?, dondé se encontrarán varios números.
  - Dentro de un conjunto un elemento no se puede repetir ese elemento, pero se puede repetir en otro conjunto.
  - Deberá de adivinar un número de la siguiente forma:
    * Al escoger un número cualquiera, debe de leer los indices en los cuales el número se encuentra.
    * Claramente si saber a que número se refieren, sólo los indices.
    * Con esos indices usted debe de ser capaz de saber que número escogió el jugador

Considere que siempre va a leer un valor máximo posible, este valor no aparecerá en ningún grupo que genere.
 
### **Ejemplos** / **Casos de prueba**

#### _Ejemplo 1_:
```
Ingrese el MAX numero:  50
De los siguientes conjuntos, escoja un numero :
1 = [1, 15, 5, 3, 45, 9, 29, 13, 41, 39, 21, 49, 27, 33, 25, 47, 31, 35, 11, 19, 23, 43, 17, 7, 37]
2 = [31, 30, 43, 11, 10, 22, 15, 34, 35, 14, 38, 7, 26, 2, 23, 18, 47, 19, 39, 6, 46, 3, 27, 42]
3 = [46, 30, 45, 6, 28, 20, 47, 5, 4, 22, 21, 12, 31, 44, 29, 7, 14, 39, 36, 23, 15, 38, 13, 37]
4 = [14, 43, 42, 30, 11, 13, 47, 46, 29, 27, 40, 44, 9, 31, 26, 28, 45, 10, 8, 25, 41, 12, 24, 15]
5 = [30, 17, 20, 24, 23, 26, 27, 19, 29, 31, 48, 22, 18, 21, 28, 25, 16, 49]
6 = [32, 47, 37, 42, 33, 44, 43, 45, 34, 40, 39, 35, 49, 41, 36, 38, 48, 46]


Ahora escriba los indices de los grupos a los cuales pertenece dicho numero: 1 2 6 4
El numero en el que estaba pensando es: 43
```

#### _Ejemplo 2_:
```
Ingrese el MAX numero:  28
De los siguientes conjuntos, escoja un numero :
1 = [7, 9, 25, 15, 5, 13, 23, 11, 1, 3, 27, 19, 21, 17]
2 = [23, 2, 27, 7, 26, 10, 11, 19, 15, 22, 14, 3, 18, 6]
3 = [20, 23, 15, 7, 6, 21, 14, 4, 5, 22, 12, 13]
4 = [11, 27, 15, 13, 12, 9, 14, 8, 25, 26, 10, 24]
5 = [25, 23, 19, 21, 17, 18, 22, 24, 27, 20, 16, 26]


Ahora escriba los indices de los grupos a los cuales pertenece dicho numero: 3 1 5
El numero en el que estaba pensando es: 21
```



###### [NOTA: ]()
  En caso de encontrar más de una forma de resolver este problema, sientase libre de comunicarla o escribirla.

