Edad = int(input("Ingrese su edad:"))

if Edad < 12:
    categoria = "Niño/a"
elif Edad >= 12 and Edad < 18:
    categoria = "Adolescente"
elif Edad >= 18 and Edad < 30:
    categoria = "Adulto/a joven"
else:
    categoria = "Adulto/a"


print(f"Usted es un {categoria}.")


