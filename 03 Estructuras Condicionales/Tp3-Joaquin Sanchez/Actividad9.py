# Solicitar al usuario la magnitud del terremoto

magnitud = float(input("Ingrese la magnitud del terremoto (escala de Richter): "))

# Clasificar la magnitud según la escala de Richter
if magnitud < 3:
    categoria = "Muy leve"
    descripcion = "Imperceptible"
elif 3 <= magnitud < 4:
    categoria = "Leve"
    descripcion = "Ligeramente perceptible"
elif 4 <= magnitud < 5:
    categoria = "Moderado"
    descripcion = "Sentido por personas, pero generalmente no causa daños"
elif 5 <= magnitud < 6:
    categoria = "Fuerte"
    descripcion = "Puede causar daños en estructuras débiles"
elif 6 <= magnitud < 7:
    categoria = "Muy Fuerte"
    descripcion = "Puede causar daños significativos"
elif magnitud >= 7:
    categoria = "Extremo"
    descripcion = "Puede causar graves daños a gran escala"
else:
    categoria = "Magnitud inválida"
    descripcion = "Por favor, ingrese un número válido."

# Imprimir el resultado por pantalla
print(f"Magnitud: {magnitud}")
print(f"Categoría: {categoria}")
print(f"Descripción: {descripcion}")