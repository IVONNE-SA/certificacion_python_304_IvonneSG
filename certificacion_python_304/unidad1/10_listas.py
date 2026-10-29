#declarando una lista
try:
    materias=["programcion","filosofia","matematicas","ingles"]
    print(materias[3])
    materias.append("Lengua y Comunicasion")
    print(materias)
    materias[1]="biologia"
    print(materias)
    materias.remove("matematicas")
    print(materias)
except IndexError:
    print("no se puede acceder aun valor que no existe")