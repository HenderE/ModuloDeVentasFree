#calculamos subtotal
subtotal = precio_producto * cantidad_productor
#Calculamos descuento
descuento = 0
if es_vip:
    descuento = subtotal * 0.10
#calculamos total
total = subtotal - descuento