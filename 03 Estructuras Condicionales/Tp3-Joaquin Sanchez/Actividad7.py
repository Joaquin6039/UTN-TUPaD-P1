# Solicitar una frase o palabra al usuario
entrada = input("Ingrese una frase o palabra: ")

# Definir las vocales
vocales = "aeiouAEIOU"

# Verificar si el último carácter es una vocal
if entrada and entrada[-1] in vocales:
    resultado = entrada + "!"
else:
    resultado = entrada

print(resultado)