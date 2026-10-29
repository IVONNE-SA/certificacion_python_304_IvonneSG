promedio=float(input("ingresa el promedio"))
#el numero ingresado es 6
if promedio<=0 :
    print("No se pueden acepatar negativos")
elif promedio<=5:
    print("Tu promedio es muy bajo")
elif promedio<5 and promedio>=7:
    print("Tu promedio es bajo")
elif promedio>7 and promedio<=9:
    print("Tu promedio es bueno")
elif promedio==10:
    print("Tu promedio exelente")
elif promedio>10:
    print("no se aceptan numeros mayores a 10")
else:
    print("Ese promedio no existe")