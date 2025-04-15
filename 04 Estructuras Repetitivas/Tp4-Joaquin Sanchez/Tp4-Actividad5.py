import random

# Generar un número aleatorio entre 0 y 9
numero_secreto = random.randint(0, 9)

intentos = 0
adivinado = False

print("¡Bienvenido al juego de adivinar el número!")
print("Intenta adivinar el número secreto entre 0 y 9.")

while not adivinado:
    try:
        intento_str = input("Ingresa tu intento: ")
        intento = int(intento_str)
        intentos += 1

        if 0 <= intento <= 9:
            if intento == numero_secreto:
                print(f"¡Felicitaciones! ¡Adivinaste el número secreto ({numero_secreto}) en {intentos} intentos!")
                adivinado = True
            elif intento < numero_secreto:
                print("El número secreto es mayor. ¡Intenta de nuevo!")
            else:
                print("El número secreto es menor. ¡Intenta de nuevo!")
        else:
            print("Por favor, ingresa un número entre 0 y 9.")

    except ValueError:
        print("Entrada inválida. Por favor, ingresa un número entero.")

print("¡Gracias por jugar!")