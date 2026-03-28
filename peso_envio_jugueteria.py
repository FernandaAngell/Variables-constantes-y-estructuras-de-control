# Sistema de calculo peso
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

# Peso de cada producto (en gramos)
PESO_PAYASO = 112
PESO_MUNECA = 75

# Solicitar datos al usuario
payasos = int(input("Ingrese la cantidad de payasos: "))
munecas = int(input("Ingrese la cantidad de muñecas: "))

# Calcular el peso total
peso_total = (payasos * PESO_PAYASO) + (munecas * PESO_MUNECA)

# Mostrar resultado
print("\n=== RESULTADO DEL ENVÍO ===")
print(f"Cantidad de payasos: {payasos}")
print(f"Cantidad de muñecas: {munecas}")
print(f"Peso total del paquete: {peso_total} gramos")