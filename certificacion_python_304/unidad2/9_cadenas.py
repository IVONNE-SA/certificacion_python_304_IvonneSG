#cadenas y concatenacion con +
cadena1='Hola'
cadena2='Mundo'
multilinea="""Esto es una cadena 
de varias lineas"""
print(cadena1 + cadena2)#print(f"{cadena1}{cadena2})
#cadenas y repeticion
eco="JA"*3
print(eco)
#cambia una cadena de mayuscula a minuscula
tu_nombre="Ivonne"
print(tu_nombre.upper())
#cambia una cadena de mayuscula a minuscula
print(tu_nombre.lower())
frase="Me gusta Programacion"
print(frase.replace("Programacion","matematicas"))
#Formato de cadenas (f-stirng)
edad=17
nombre="ivon"
mensaje=f"Hola, me llamo {nombre}\ny tengo {edad} años"
print(mensaje)
texto= "¡Felicidades por aun continuar en el CECY!!!"
cantidad_caracteres=len(texto)
print(cantidad_caracteres)
#comprobar si un texto contiene una palabra
oracion="Aprender python es divertido"
if "java" in oracion:
    print("Encontrado")
else:
    print("No esta")
    #validar contenido en una cadena
Nlista="ivon"
print(Nlista.isalpha())#texto
print(Nlista.isdigit())#numero
