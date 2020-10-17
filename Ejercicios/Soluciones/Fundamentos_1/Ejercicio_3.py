"""
 Hecho por: Leonardo Fernández Ríos
 Ejercicio 3
 Versión beta.
"""

print('Problema versión novato:')
print('*')
print('* *')
print('* * *')
print('* * * *')
print('* * * * *')
print('* * * *')
print('* * *')
print('* *')
print('*')

print('\nProblema versión pro:\n')
n = int(input('Ingrese un numero, menor a 50, de preferencia.\n'))
print('')
for i in range(1,n+1):
    print('* '*i)
for i in range(1,n):
    print('* '*(n-i))

