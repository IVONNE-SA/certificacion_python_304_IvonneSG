tabla =[
    ["Nombre","Edad","calificasion"],
    ["sofia",16,7.0],
    ["pedro",17,8.0],
    ["ivonne",16,7.0],
    ["ivan",16,8.0],
    ["litzy",15,9.0],
    ["diana",16,8.0],
    ["sherlin",16,9.0],
    ["amanda",16,9.0],
    ["eusebia",15,8.0],
    ["nora",16,7.0]
]
nombre=input("introduce tu nombre")
filas=len(tabla)
columnas=len(tabla[0])
for i in range(filas):
    for j in range(columnas):
        if tabla[i][j] == nombre:
            print(f"Nombre encontrado en la posición [{i}][{j}]")
