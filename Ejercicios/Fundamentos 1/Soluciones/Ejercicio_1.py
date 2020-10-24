"""
 Hecho por: Leonardo Fernández Ríos
 Ejercicio 1
 Versión beta.
"""

numero = input('Ingrese un número:\n')
maximo = numero
minimo = numero
while(numero!='Fin'):
    numero = input('Ingrese un número:\n')
    if(numero!='Fin' and maximo < numero):
        maximo = numero
    if(numero!='Fin' and minimo > numero):
        minimo = numero

print('El maximo número leído fue:\n')
print(maximo)
print('\n')
print('El minimo número leído fue:\n')
print(minimo)
print('\n')
