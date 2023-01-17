import re

text = "El artista mira hacia arriba. \"Siempre va a tratarse de Tree Fiddy\""

# buscar "tree fiddy", "3.50" o "three fifty" en el texto
result = re.search("tree fiddy|3\.50|three fifty", text, re.IGNORECASE)

if result:
    print("Encontrado el Monstruo del Lago Ness!")
else:
    print("No se encontró el Monstruo del Lago Ness.")
