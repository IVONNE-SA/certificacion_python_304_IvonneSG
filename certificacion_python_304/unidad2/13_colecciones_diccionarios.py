#creando un diccionario
personas={
    "nombre":"ivon",
    "edad":16,
    "profesion":"programador",
    "estudiante":False
}
print(personas)
#accediendo a un valor especifico
print(personas["edad"])
#se puede usar por metodo(get)
#es util por que no marca error si el valor no existe
print(personas.get("profesion"))
#modificar un valor existente
personas["edad"]=17
print(personas["edad"])