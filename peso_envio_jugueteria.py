
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#La juguetería “Mundo Mágico” realiza envíos nacionales
#en su campaña “Sonrisas por correo”. Para calcular el costo del envío,
#se necesita conocer el peso total del pedido.
#Datos:
#- Cada payaso de tela pesa 112 gramos.
#- Cada muñeca clásica pesa 75 gramos.
#El programa debe:
#- Solicitar la cantidad de payasos y muñecas en el pedido.
#- Calcular y mostrar el peso total en gramos con un mensaje claro.

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
#Realizado por Maria Fernanda Tolosa Angel
