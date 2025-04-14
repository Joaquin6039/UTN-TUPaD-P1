Contra = input("Ingrese una contraseña de 8 a 14 caracteres:")

if len(Contra) >= 8 and len(Contra) <= 14:
    print(f"Ha ingresado una contraseña correcta")
else:
    print(f"Por favor, ingrese una contraseña de entre 8 y 14 caracteres")

