#presentacion
print("=" * 19)
print("Registro de venta")
print("=" * 19)

#pedimos datos al usuario
nombre_cliente = input("Ingresa tu nombre: ")
precio_producto = float(input("Ingresa el valor de tu producto: "))
cantidad_productor = int(input("Ingresa la cantidad: "))
cliente_vip = input("Eres cliente VIP? (si/no): ")

es_vip = cliente_vip.lower() == "si"