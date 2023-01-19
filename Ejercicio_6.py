import math

def max_rope_length(diameter, percentage):
    # Calcular el radio del parche circular de hierba
    radius = diameter / 2
    # Calcular el área del parche circular de hierba
    area = math.pi * (radius ** 2)
    # Calcular el área permitida para Burro
    allowed_area = area * percentage
    # Calcular la longitud máxima de la cuerda utilizando la circunferencia del área permitida para Burro
    max_length = 2 * math.pi * math.sqrt(allowed_area / math.pi)
    # Devolver la longitud de la cuerda en pasos de ogro enteros
    return int(max_length)

# Ejemplo de uso
diameter = 50
percentage = 0.5
print("Longitud máxima de la cuerda:", max_rope_length(diameter, percentage), "pasos de ogro")