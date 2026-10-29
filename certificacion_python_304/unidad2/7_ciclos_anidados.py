#ciclo externo para el numero de la base de la tabla
for i in range(1,5):
    print(f"---Tabla del {i}---")
    #ciclo interno nos multipica la base (i)por el numero(j)
    for j in range(1,11):
        print(f"{i} x {j} = {i*j}")#f concatena texto con numeros
    print(f"aqui termina la tabla del {i}")