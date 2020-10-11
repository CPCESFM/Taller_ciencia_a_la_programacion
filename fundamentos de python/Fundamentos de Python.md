# Fundamentos de Python

[toc]

Aprender un lenguaje de programación, es como aprender un nuevo idioma, y para hablarlo bien debemos aprender sus reglas, en estas notas aprenderemos los fundamentos de Python. Empezaremos por variables, estructuras de control y ciclos. 

## Variables

Las variables son cajas que nos permiten guardad cualquier tipo de valores, declarar variables en python es bastante sencillo, por ejemplo

```python
numero = 18
```

de la forma anterior creamos una variable de nombre *numero* que guarda el valor *18*, hay un tercer elemento en la expresión de arriba el cual es el signo de `=` . Él cual se conoce como el operador de asignación el cual guarda el valor de la derecha, en la variable de la izquierda. Ahora estudiaremos ambos lados del operador, empecemos con el lado izquierdo, el cual es el nombre de la variable, este puede ser cualquier cosa como *perro, gato, manzana*, sin embargo hay algunas reglas que debemos seguir,

- El nombre de una variable debe empezar con una letra o un guion bajo.
- El nombre de una variable solo puede contener, letras(A-z), números(0-9) y guiones bajos( _ ).
- El nombre de una variable es sensible a mayúsculas y  minúsculas, por lo que es distinto *var* de *Var*

Aunque podemos nombrar las variables como queremos es recomendable usar nombres representativos para mejor lectura del programa. 

Ahora continuemos con el lado derecho del operador, el cual es el valor que puede guardar una variable, por ejemplos números, texto, valores de verdad u objetos. **Es importante conocer los tipos de datos, aunque python puede identificarlos de forma automática.**

### Numéricos

Empecemos con los datos de tipo numérico, distinguiremos 3 tipos de datos numéricos,

- **int**, este tipo de datos guardan valores de tipo entero, es decir sin decimales, por ejemplo, `5`, `7` o `2020`.
- **float**, este tipo de datos guardan valores con punto decimal, por ejemplo `3.1415`, `-1.42` o `0.123`.
- **complex**, es tipo de datos guardan valores de números complejos , por ejemplo `3.1415+ 5i`.

podemos hacer esto en python de la siguiente manera,

```python
edad = 23  
estatatura = 1.80
```

python identifica el primer valor como un entero pues no tiene punto decimal, y sabe que *estatura* es float pues tiene decimales.

### Cadenas de texto

Otro tipo de datos son las cadenas de texto, estas nos ayudan a guardar palabras, carácteres o texto, para representarlas en python las encerramos entre comillas, podemos hacer esto en python de la siguiente manera,

```python
nombre = "Pancho"
letra = "c"
```

### Booleanos

Este tipo de datos solo puede tomar dos valores, verdadero o falso, en la practica se usan para definir condiciones por ejemplo cuando una luz esta prendida o apagada, en python representamos estos valores con las palabras en inglés `True` y `False`, **es importante que la primera letra sea mayúscula**.

```python
Luz = True
Hambre = False
```

Una vez que tenemos variables podemos combinarlas para crear nuevas variables o nuevos valores, así introducimos los operadores

## Operadores

Los operadores nos permiten transformar o combinar variables, los operadores que podemos aplicar sobre un variable depende del tipo de esta. Los principales operadores  son los aritméticos, los lógicos y de comparación.

### Operadores aritméticos

Este tipo de operadores nos permite combinar y transformar datos de tipo numérico y son los que aprendemos durante nuestra educación básica, 

| Nombre          | Operador | Ejemplo    |
| --------------- | -------- | ---------- |
| Suma            | +        | 5+2 = 10   |
| Resta           | -        | 5-2 = 3    |
| División        | /        | 10/4 = 2.5 |
| División entera | //       | 10/4 = 2   |
| Multiplicación  | *        | 5*3 = 15   |
| Modulo          | %        | 5 % 3 = 2  |
| Exponenciación  | **       | 2**2 = 4   |

### Operadores lógicos

Este tipo de operadores nos ayudan a trabajar con valores de verdad, estos operadores se muestran en la siguiente tabla

| Nombre     | Operador | Ejemplo                 |
| ---------- | -------- | ----------------------- |
| Conjunción | and      | False and True = True   |
| Disyunción | or       | False and False = False |
| Negación   | not      | not True = False        |

**agregar ejemplo

### Operadores de comparación

Este tipo de operadores nos ayudan a comparar, es importante notar que los objetos o variables a comparar deben ser del mismo tipo, por ejemplo no tiene sentido comparar un numero con una cadena de texto. Este tipo de operadores regresan un valor booleano por lo que podemos combinarlo con operadores lógicos para crear condiciones complejas. La siguiente tabla muestra estos operadores

| Nombre            | Operador | Ejemplo                  |
| ----------------- | -------- | ------------------------ |
| Igualdad          | ==       | 2 == 3 => False          |
| Desigualdad       | !=       | "Hola" != "hola" => true |
| Mayor que         | >        | 0 > -3                   |
| Menor que         | <        | 10 < 5                   |
| Menor o igual que | <=       | 10 <= 11                 |
| Mayor o igual que | >=       | 10>=10                   |

**Ejercicio**

```
crear un programa con la información personal, nombre, edad, estatura, etc...
```

Las variables son importantes pues nos ayudan a guarda datos e información pero para desarrollar programas cada vez mas complejos debemos introducir nuevas estructuras,  las primeras que introduciremos serán las estructuras de control.

## Estructuras de control

Las estructuras de control nos ayudan a tomar decisiones basadas en algún valor lógico, es hacer una pregunta a la computadora que se responde con un **sí** o un **no**, por ejemplo querer comprar algo podemos preguntarnos ¿Tengo dinero?, esto lo escribimos en python de la siguiente manera,

```python
if(dinero<=0):
    print("Estas quebrado :C")
```

el ejemplo anterior imprime la oración *Estas quebrado :C* si la variable *dinero* es menor o igual que 0, veamos las partes de esta estructura, primero utilizamos la palabra reservada `if` seguida de uno condición lógica, lo cual podemos interpretarla como *si la condición es verdadera entonces ejecuta lo siguiente* en caso de que la condición sea falsa no se ejecutara el siguiente bloque. 

Antes de continuar es importante notar algunos detalles, los **dos puntos** al terminar el *if* indican que esa instrucción ha terminado y las siguientes instrucciones son las que se ejecutaran en caso de que la condición resulte verdadera, el segundo detall}e a notar es la **indentación** o **sangrado** de las siguientes líneas de código, esto es el espacio que hay entre el comienzo el margen del texto y el texto. En python a diferencia de otros lenguajes se usan espacios o tabuladores en lugar de llaves para agrupar bloques de código, por lo cual es importante cuidar el sangrado y que se usen **solamente** espacios o tabuladores.

Ahora que pasa si queremos ejecutar instrucciones en caso de la condición sea falsa para ello usaremos la palabra reservada `else` . Complementando el ejemplo anterior,

```python
if(dinero<=0):
    print("Estas quebrado :C")
else:
    print("A gastar >:D")
```

Algo que podemos observar es que después del `else` no hay ninguna condición, ya que no es necesario, pues este bloque de código soló se ejecutará si la condición en el `if `es falsa, esto puede resumirse en la siguiente nota **cada else es pareja de un if**