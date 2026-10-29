tabla=int(input("Ingresa la tabla de multiplicar que desees saber"))
if tabla>=1 and tabla<=10:
    for i in range(1,11):
        resultado=tabla*i
        print(tabla,"x",i,"=",resultado)
else:
    print("el numero deber entre 1 y 10")