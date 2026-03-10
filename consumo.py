# Sistema de clasificación de consumo eléctrico - LowCost
#MARIA FERNANDA TOLOSA ANGEL
#La empresa de energía “LowCost” necesita un sistema
#que permita clasificar el consumo mensual en kWh y aplicar los
#ajustes correspondientes en la facturación.
#El programa debe:
#1) Solicitar al usuario el consumo mensual en kWh.
#2) Clasificar el consumo en:
#- Bajo: menos de 150 kWh.
#- Medio: entre 150 kWh y 350 kWh.
#- Alto: más de 350 kWh.
#3) Calcular el valor base del consumo usando el costo por kWh:
#Costo por kWh = 𝟑𝟐𝟎. 𝟓 COP
#4) Aplicar los ajustes:
#a. Consumo bajo: descuento del 5%.
#b. Consumo medio: sin ajuste.
#c. Consumo alto: recargo del 12%
#Salida esperada:
#- Categoría del consumo.
#- Valor base.
#- Porcentaje de descuento o recargo aplicado.
#- Valor final a pagar.
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

#Realizado por Maria Fernanda Tolosa Angel.

