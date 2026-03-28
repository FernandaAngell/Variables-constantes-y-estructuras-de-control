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