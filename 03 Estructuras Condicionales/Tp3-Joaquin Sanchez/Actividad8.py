# Solicitar al usuario que ingrese su nombre
nombre = input("Ingrese su nombre: ")

# Solicitar al usuario que elija una opción
opcion = input("Ingrese 1 para mayúsculas, 2 para minúsculas o 3 para primera letra mayúscula: ")

# Realizar la transformación
if opcion == "1":
    nombre_transformado = nombre.upper()
elif opcion == "2":
    nombre_transformado = nombre.lower()
elif opcion == "3":
    nombre_transformado = nombre.title()
else:
    nombre_transformado = "Opción inválida"

print("Resultado:", nombre_transformado)