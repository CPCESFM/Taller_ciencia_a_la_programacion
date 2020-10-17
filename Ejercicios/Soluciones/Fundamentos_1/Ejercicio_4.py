"""
 Hecho por: Leonardo Fernández Ríos
 Ejercicio 4
 Versión beta.
"""

numero = input('Ingresa un número\n')
print('Su número es:\n' + numero)
print('El número al revés es:')
for i in range(1,len(numero)+1):
    print(numero[-i],end='')
print('\n')