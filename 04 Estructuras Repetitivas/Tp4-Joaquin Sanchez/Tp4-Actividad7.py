try:
    limite = int(input("Ingrese un número entero positivo: "))

    if limite <= 0:
        print("Por favor, ingrese un número entero positivo.")
    else:
        suma = 0
        for numero in range(limite + 1):
            suma += numero
        print(f"La suma de los números desde 0 hasta {limite} es: {suma}")

except ValueError:
    print("Entrada inválida. Por favor, ingrese un número entero.")