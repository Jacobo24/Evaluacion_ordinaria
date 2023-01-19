def solve_nonogram(clues):
    # Pistas es una tupla de dos elementos, cada uno de ellos es una lista de 5 elementos
    col_clues, row_clues = clues
    # Crear una matriz de 5x5 con todos los elementos inicializados en '_'
    matrix = [['_' for _ in range(5)] for _ in range(5)]
    # Rellene las celdas según las pistas de la columna
    for col, clues in enumerate(col_clues):
        current_clue_index = 0
        current_clue = clues[current_clue_index]
        current_clue_count = 0
        for row in range(5):
            if matrix[row][col] == '_':
                matrix[row][col] = '0'
                current_clue_count += 1
                if current_clue_count == current_clue:
                    current_clue_index += 1
                    if current_clue_index < len(clues):
                        current_clue = clues[current_clue_index]
                        current_clue_count = 0
                    else:
                        break
    # Rellene las celdas en función de las pistas de fila
    for row, clues in enumerate(row_clues):
        current_clue_index = 0
        current_clue = clues[current_clue_index]
        current_clue_count = 0
        for col in range(5):
            if matrix[row][col] == '_':
                matrix[row][col] = '0'
                current_clue_count += 1
                if current_clue_count == current_clue:
                    current_clue_index += 1
                    if current_clue_index < len(clues):
                        current_clue = clues[current_clue_index]
                        current_clue_count = 0
                    else:
                        break
    # Use la deducción lógica para completar las celdas restantes
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == '_':
                matrix[row][col] = '1'
    return matrix

clues = ([2, 1], [1, 1, 1], [2, 1], [1, 1, 1], [2, 1]), ([1, 1], [2, 2], [3, 1], [2, 2], [1, 1])

solved_nonogram = solve_nonogram(clues)

for row in solved_nonogram:
    print(row)

# Código más complejo para que me de otra matriz