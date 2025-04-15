total = 0
print("Ingrese números enteros para sumar (ingrese 0 para detener):")

while True:
    entrada = input("Ingrese un número: ")
    numero = int(entrada)

    if numero == 0:
        break  # Salir del bucle si el usuario ingresa 0
    else:
        total += numero
        print(f"Subtotal actual: {total}")

print(f"\nTotal acumulado: {total}")
print("Programa finalizado.")
