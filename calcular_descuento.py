def calcular_descuento(monto_total, porcentaje_descuento=10):
    descuento = monto_total * (porcentaje_descuento / 100)
    return descuento

# Llamada 1: Proporcionando solo el monto total de la compra
monto_compra1 = 100
descuento1 = calcular_descuento(monto_compra1)
monto_final1 = monto_compra1 - descuento1
print("Monto de descuento:", descuento1)
print("Monto final a pagar después del descuento:", monto_final1)

# Llamada 2: Proporcionando tanto el monto total de la compra como el porcentaje de descuento
monto_compra2 = 200
porcentaje_descuento2 = 20
descuento2 = calcular_descuento(monto_compra2, porcentaje_descuento2)
monto_final2 = monto_compra2 - descuento2
print("Monto de descuento:", descuento2)
print("Monto final a pagar después del descuento:", monto_final2)
