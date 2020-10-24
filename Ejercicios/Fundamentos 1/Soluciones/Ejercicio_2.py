"""
 Hecho por: Leonardo Fernández Ríos
 Ejercicio 2
 Versión beta.
"""
print(' 1,')
for i in range(2,99):
    if(i%3!=0 and i%5!=0):
        print(' '+str(i)+',')
    elif (i%3==0 and i%5!=0):
        print(' Fizz,')
    elif (i%3!=0 and i%5==0):
        print(' Buzz,')
    else:
        print(' Fizz Buzz,')

print(' Buzz')