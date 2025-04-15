numeroinvertido = ""

while True:
    try:
        numerostr = input("Ingrese un numero:")
        numero = int(numerostr)
        cantidadnumeros = len(numerostr)
        break
    except ValueError:
        print("Ingrese un numero entero valido")

for i in range(cantidadnumeros - 1, -1, -1):
    numeroinvertido += numerostr[i]

print(f"Tu numero invertido es: {numeroinvertido}")