# Definir variables
pares = 0
impares = 0
positivos = 0
negativos = 0

print("Ingrese 100 números enteros:")

for i in range(100):
    while True:
        try:
            entrada = input(f"Ingrese el número {i + 1}: ")
            numero = int(entrada)
            break  # Salir del bucle interno si la entrada es válida
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

    if numero % 2 == 0:
        pares += 1
    else:
        impares += 1

    if numero > 0:
        positivos += 1
    elif numero < 0:
        negativos += 1

print("\nResultados:")
print(f"Cantidad de números pares: {pares}")
print(f"Cantidad de números impares: {impares}")
print(f"Cantidad de números positivos: {positivos}")
print(f"Cantidad de números negativos: {negativos}")