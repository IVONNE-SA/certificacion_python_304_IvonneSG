carrito=[]
n_productos=int(input("Ingresa el numero de productos"))
for i in range (n_productos):
    productos=input("Ingresa el producto a tu carrito")
    carrito.append(productos)
print("Lista creada correctamente")
print(f"tu carrito contiene{carrito}")
carrito[0]="chetos"
print(carrito[0])
print(carrito[1])
print(carrito)