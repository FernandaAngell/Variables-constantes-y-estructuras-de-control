# Sistema de clasificación de consumo eléctrico - LowCost
#MARIA FERNANDA TOLOSA ANGEL
#213022_277
#FUNDAMENTOS DE PROGRAMACION
#PROGRAMA...
#CODIGO FUENTE: AUTORIA PROPIA

COSTO_KWH = 320.5  

consumo = float(input("Ingrese el consumo mensual en kWh: "))

if consumo < 150:
    categoria = "Bajo consumo"
    ajuste = -0.05
elif consumo <= 350:
    categoria = "Consumo medio"
    ajuste = 0
else:
    categoria = "Alto consumo"
    ajuste = 0.12

valor_base = consumo * COSTO_KWH
valor_ajuste = valor_base * ajuste
valor_final = valor_base + valor_ajuste

print("\n--- FACTURACIÓN LOWCOST ---")
print(f"Categoría del consumo: {categoria}")
print(f"Valor base: ${valor_base:,.2f}")

if ajuste < 0:
    print("Descuento aplicado: 5%")
elif ajuste > 0:
    print("Recargo aplicado: 12%")
else:
    print("Ajuste aplicado: 0%")

print(f"Valor final a pagar: ${valor_final:,.2f}")

