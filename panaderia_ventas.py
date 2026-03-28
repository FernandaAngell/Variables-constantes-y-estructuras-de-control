
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#Una panadería vende los siguientes productos:
#Panes:
#- Integral: $2.000
#- Francés: $3.000
#- Queso: $1.000
#Pasteles:
#- Chocolate: $6.000
#- Manzana: $5.000
#El programa debe:
#- Mostrar los productos y precios.
#- Permitir al cliente seleccionar cantidad por producto.
#- Calcular el total a pagar.
#- Si el total supera $10.000, aplicar descuento del 20%.
#- Mostrar el total final después del descuento (si aplica).

# Precios
PAN_INTEGRAL = 2000
PAN_FRANCES = 3000
PAN_QUESO = 1000
PASTEL_CHOCOLATE = 6000
PASTEL_MANZANA = 5000

# Mostrar menú
print("=== PANADERÍA ===")
print("Panes:")
print("1. Integral - $2000")
print("2. Francés - $3000")
print("3. Queso - $1000")
print("\nPasteles:")
print("4. Chocolate - $6000")
print("5. Manzana - $5000")

# Cantidades
cant_integral = int(input("\nCantidad de pan integral: "))
cant_frances = int(input("Cantidad de pan francés: "))
cant_queso = int(input("Cantidad de pan de queso: "))
cant_chocolate = int(input("Cantidad de pastel de chocolate: "))
cant_manzana = int(input("Cantidad de pastel de manzana: "))

# Calcular total
total = (
    cant_integral * PAN_INTEGRAL +
    cant_frances * PAN_FRANCES +
    cant_queso * PAN_QUESO +
    cant_chocolate * PASTEL_CHOCOLATE +
    cant_manzana * PASTEL_MANZANA
)

# Aplicar descuento
if total > 10000:
    descuento = total * 0.20
    total_final = total - descuento
else:
    descuento = 0
    total_final = total

# Mostrar resultados
print("\n=== FACTURA ===")
print(f"Total sin descuento: ${total}")
print(f"Descuento: ${descuento}")
print(f"Total a pagar: ${total_final}")

#Realizado por Maria Fernanda Tolosa Angel
