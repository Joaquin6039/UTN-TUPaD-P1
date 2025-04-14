# Solicitar información al usuario
hemisferio_usuario = input("¿En qué hemisferio se encuentra? (N/S): ")
mes_usuario = input("¿Qué mes del año es?: ")
dia_usuario = int(input("¿Qué día es?: "))

if hemisferio_usuario.upper() == 'N':
    if (mes_usuario == 'diciembre' and dia_usuario >= 21) or \
       (mes_usuario == 'enero') or \
       (mes_usuario == 'febrero') or \
       (mes_usuario == 'marzo' and dia_usuario <= 20):
        estacion_actual = "Invierno"
    elif (mes_usuario == 'marzo' and dia_usuario >= 21) or \
         (mes_usuario == 'abril') or \
         (mes_usuario == 'mayo') or \
         (mes_usuario == 'junio' and dia_usuario <= 20):
        estacion_actual = "Primavera"
    elif (mes_usuario == 'junio' and dia_usuario >= 21) or \
         (mes_usuario == 'julio') or \
         (mes_usuario == 'agosto') or \
         (mes_usuario == 'septiembre' and dia_usuario <= 20):
        estacion_actual = "Verano"
    elif (mes_usuario == 'septiembre' and dia_usuario >= 21) or \
         (mes_usuario == 'octubre') or \
         (mes_usuario == 'noviembre') or \
         (mes_usuario == 'diciembre' and dia_usuario <= 20):
        estacion_actual = "Otoño"
    else:
        estacion_actual = "Fecha inválida"
elif hemisferio_usuario.upper() == 'S':
    if (mes_usuario == 'diciembre' and dia_usuario >= 21) or \
       (mes_usuario == 'enero') or \
       (mes_usuario == 'febrero') or \
       (mes_usuario == 'marzo' and dia_usuario <= 20):
        estacion_actual = "Verano"
    elif (mes_usuario == 'marzo' and dia_usuario >= 21) or \
         (mes_usuario == 'abril') or \
         (mes_usuario == 'mayo') or \
         (mes_usuario == 'junio' and dia_usuario <= 20):
        estacion_actual = "Otoño"
    elif (mes_usuario == 'junio' and dia_usuario >= 21) or \
         (mes_usuario == 'julio') or \
         (mes_usuario == 'agosto') or \
         (mes_usuario == 'septiembre' and dia_usuario <= 20):
        estacion_actual = "Invierno"
    elif (mes_usuario == 'septiembre' and dia_usuario >= 21) or \
         (mes_usuario == 'octubre') or \
         (mes_usuario == 'noviembre') or \
         (mes_usuario == 'diciembre' and dia_usuario <= 20):
        estacion_actual = "Primavera"
    else:
        estacion_actual = "Fecha inválida"
else:
    estacion_actual = "Hemisferio inválido"

# Imprimir el resultado
print(f"En el hemisferio {hemisferio_usuario.upper()} el {dia_usuario} de {mes_usuario.capitalize()} es {estacion_actual}.")