#el mapa del tesoro
mapa=[
    [".",".",".","."],
    [".",".","X","."],
    [".",".",".","."],
    [".",".",".","."]
]
filas=len(mapa)
columnas=len(mapa)
#recorriendo la matriz en ciclos anidados
#ciclo externo para manejar filas(i)
for i in range(filas):
    #ciclo externo para manejar columnas(j)
    for j in range(columnas):
        #verificamos si encontramos el tesoro
        if mapa[i][j]=="X":
            print(f"Mapa encontrado en la posición [{i}][{j}]")