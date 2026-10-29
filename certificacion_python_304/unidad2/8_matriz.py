#creando una matriz
numeros=[
    [1,2,3],#fila 0
    [4,5,6],#fila 1
    [7,8,9]#fila 2
]
#obteniendo el numero de filas
filas=len(numeros)#filas = 3
#obteniendo elnumero de columnas
columnas=len(numeros[0])
#ciclo externo para los indices de las filas(i)
for i in range(filas):
    #ciclo interno para los indices de las columnas(j)
    for j in range(columnas):
        print(f"[{i}] [{j}] = {numeros[i][j]}")