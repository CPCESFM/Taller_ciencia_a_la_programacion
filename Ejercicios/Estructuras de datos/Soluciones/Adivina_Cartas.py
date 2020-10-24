"""
Hecho por: Leonardo Fernández Ríos
23/10/2020
Juego de las cartas mágicas
"""

import random

### Intentemos usar lo aprendido, y hagamos funciones
### #SinMiedoAlExito

def log2Ceil(numero):
    """ Devuelve la función techo de log_2(numero) """
    exponente = 1
    base = 2
    while base<numero:
        base *= 2
        exponente += 1
    return exponente

#Decodificación del numero
def respuesta( index , COTA_S ):
    """ Devuelve la respuesta del problema """
    res = 0
    #Buscaremos todos los indices posibles en nuestra cadena con indices
    for i in range(0,log2Ceil(COTA_S)):
        #Aquí buscamos cada indice en la cadena, justo como cuando
        #Buscabamos en la tupla
        if str(i+1) in index:
            res += (1<<i)
    return res

#  Primero leamos el numero de cartas con el que
#  vamos a trabajar

n_max = int(input('Ingrese el MAX numero:  '))
# Creamos nuestra lista vacia con las condiciones magicas
lista = [[] for i in range(0,log2Ceil(n_max))]

# Procedemos a llenar nustras listas
for i in range(1,n_max):
    """Así es utilizaremos la mascara de bits de los números
    para poder distribuir estos de una forma #M A G I C A# """
    bits = 1
    pos  = 0
    while(bits<=i):
        # Si el bit esta prendido entonces se mete a esa lista
        if(i&bits):
            lista[pos].append(i)
        # Al hacer esto codificamos el numero
        bits <<= 1
        pos += 1

print('De los siguientes conjuntos, escoja un numero :')

for i in range(0,len(lista)):
    """ Ordenamos al azar para dar mistisismo """
    random.shuffle(lista[i])
    #Imprimimos nuestra lista
    print(str(i+1), end = ' = ')
    print(lista[i])

indices = input('\n\nAhora escriba los indices de los grupos a los cuales pertenece dicho numero: ')
#Procedemos a decodificar el numero
print('El numero en el que estaba pensando es: ' + str(respuesta(indices,n_max)) + '\n' )

