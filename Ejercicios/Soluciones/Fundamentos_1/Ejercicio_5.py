"""
 Hecho por: Leonardo Fernández Ríos
 Ejercicio 5
 Versión beta.
"""

edad_hum = float(input('Ingrese la edad del perro en años humanos:\n'))

if( edad_hum>=0.0 and edad_hum<=21.0 ):
    print(str( edad_hum/10.5 ))
else:
    print(str(2 + (edad_hum-21.0)/4.0))