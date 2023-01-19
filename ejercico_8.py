import re
import random

def main():
    frases = ["El artista mira hacia arriba. \"Siempre va a tratarse de Tree Fiddy\"",
              "¿Cuál es el precio de una cerveza?",
              "¿Cuánto cuesta una habitación para una noche?",
              "¿Puedo tener una cucharada de azúcar?",
              "¿Qué tal si nos tomamos una cerveza juntos?"]

    # elegir una frase al azar
    frase_elegida = random.choice(frases)
    print("Frase elegida: ", frase_elegida)

    # buscar "tree fiddy", "3.50" o "three fifty" en la frase elegida
    result = re.search("tree fiddy|3\.50|three fifty", frase_elegida, re.IGNORECASE)

    if result:
        print("Encontrado el Monstruo del Lago Ness!")
    else:
        print("No se encontró el Monstruo del Lago Ness.")

    main()
