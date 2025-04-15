from statistics import mean
# Definir la lista de numeros
numeros = []

# Pedir los numeros al usuario
for i in range (100):
    while True:
        try:
            numero_ingresadostr = input(f"Ingrese el número {i + 1}: ")
            numero_ingresado = int(numero_ingresadostr)
            numeros.append(numero_ingresado)
            break
        except ValueError:
            print("Entrada inválida. Por favor, ingrese un número entero.")

#Calcular la media e imprimirla por pantalla
media = mean(numeros)
print(f"La media es {media}")
