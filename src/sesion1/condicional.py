gusto_cebolla = False

if (gusto_cebolla):
    print("agregar cebolla")
else:
    print("sin cebolla")

#comentarios una linea
""" 
este
es
un 
comentario
de muchas 
lineas
"""



""" 10 - 9 A
    9 - 8  B
    8 - 7  C
    7 - 6  D
    < 6    F
"""
calificacion = 8.5
if(calificacion > 9):
    print("A")
else:
    if(calificacion > 8):
        print("B")
    else:
        if(calificacion > 7):
            print("C")
        else:
            if(calificacion > 6):
                print("D")
            else:
                print("F")

if(calificacion > 9):
    print("A")
elif(calificacion > 8):
    print("B")
elif(calificacion > 7):
    print("C")
elif(calificacion > 6):
    print("D")
else:
    print("F")

