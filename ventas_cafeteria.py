
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA


#Una tienda de café desea automatizar el registro de
#ventas diarias. El administrador registra las ventas en tres momentos:
#mañana, tarde y noche.
#El programa debe:
#1. Solicitar el valor de las ventas en cada momento.
#2. Calcular el total de ventas del día.
#3. Comparar el total con la meta diaria de $150.000.
#Salida esperada:
#- Total vendido.
#- Mensaje:
#✓ “Meta alcanzada” si el total ≥ 150.000.
#✓ “Meta no alcanzada” si el total < 150.000.

# Meta diaria
META = 150000

# Solicitar ventas
manana = float(input("Ingrese las ventas de la mañana: "))
tarde = float(input("Ingrese las ventas de la tarde: "))
noche = float(input("Ingrese las ventas de la noche: "))

# Calcular total
total = manana + tarde + noche

# Mostrar resultados
print("\n=== REPORTE DE VENTAS ===")
print(f"Total vendido: ${total}")

# Comparar con la meta
if total >= META:
    print("Meta alcanzada ✅")
else:
    print("Meta no alcanzada ❌")

#Realizado por Maria Fernanda Tolosa Angel
