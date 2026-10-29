#declarando una lista
try:
    Alumnos=["Sofia","Ivonne","Litzy","Sherlin","Eusebia"]
    Calificasion=["7.8","8.0","9.2","8.8","8.7"]
    print("Alumnos:",Alumnos[2] , "Calificasion:",Calificasion[2])
    print("Alumnos:",Alumnos[4] , "Calificasion:",Calificasion[4])
except IndexError:
    print("no se puede acceder aun valor o calificasion que no existe")