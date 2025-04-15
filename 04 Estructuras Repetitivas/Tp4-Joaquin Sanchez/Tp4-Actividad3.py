# Definimos variables
valor_inicial = int(input("Ingrese el valor inicial: "))
valor_final = int(input("Ingrese el valor final: "))

suma = 0
if valor_inicial < valor_final - 1:
    for i in range(valor_inicial + 1, valor_final):
        suma += i
    print(f"La suma de los enteros entre {valor_inicial} y {valor_final} (excluyéndolos) es: {suma}")       
else:
    print(f"No hay enteros entre {valor_inicial} y {valor_final} (excluyéndolos).")