# Importar librerias
from statistics import mode, median, mean
import random

# Definir la lista de números aleatorios
numero_aleatorios = [random.randint(1, 100) for i in range(50)]

# Calcular la moda, mediana y media
modee = mode(numero_aleatorios)
mediann = median(numero_aleatorios)
meann = mean(numero_aleatorios)

# Comparar los parámetros estadísticos para determinar el sesgo
print(f"Lista de números aleatorios: {numero_aleatorios}")
print(f"Moda: {modee}")
print(f"Mediana: {mediann}")
print(f"Media: {meann}")

if meann > mediann and mediann > modee:
    print(f"Sesgo positivo o a la derecha")
elif meann < mediann and mediann < modee:
    print(f"Sesgo negativo o a la izquierda")
elif meann == mediann == modee:
    print(f"Sin sesgo")
else:
    print(f"No se puede determinar el sesgo claramente con los criterios dados.")

