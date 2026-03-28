# Sistema de calculo peso
#MARIA FERNANDA TOLOSA ANGEL
#FUNDAMENTOS DE PROGRAMACION
#CODIGO FUENTE: AUTORIA PROPIA

#Diseñe un programa para calcular el valor final de un
#producto según su categoría.
#Requisitos:
#- Definir una constante IVA = 0.19.
#- Solicitar el precio base del producto.
#✓ Si el precio ≤ 0, mostrar error y finalizar.
#- Solicitar el código de categoría:
#✓ Producto básico: no paga IVA.
#✓ Producto estándar: paga IVA del 19%.
#✓ Producto de lujo: paga IVA del 19% + recargo del 5%.
#- Si el código es inválido, mostrar error y finalizar.
#- Calcular y mostrar el valor final según la categoría.


# Constante
IVA = 0.19

# Solicitar precio
precio = float(input("Ingrese el precio base del producto: "))

# Validar precio
if precio <= 0:
    print("Error: el precio debe ser mayor que 0 ❌")
else:
    # Solicitar categoría
    print("\nSeleccione la categoría:")
    print("1. Básico (sin IVA)")
    print("2. Estándar (IVA 19%)")
    print("3. Lujo (IVA 19% + 5% recargo)")
    
    categoria = input("Ingrese el código (1, 2 o 3): ")

    # Calcular según categoría
    if categoria == "1":
        total = precio

    elif categoria == "2":
        total = precio + (precio * IVA)

    elif categoria == "3":
        total = precio + (precio * IVA) + (precio * 0.05)

    else:
        print("Error: categoría inválida ❌")
        exit()

    # Mostrar resultado
    print("\n=== RESULTADO ===")
    print(f"Precio base: ${precio}")
    print(f"Valor final: ${total}")

#Realizado por Maria Fernanda Tolosa Angel
