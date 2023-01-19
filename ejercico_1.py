def solve_nonogram(clues):
    # pistas es una tupla de dos elementos, cada uno de ellos es una lista de 5 elementos
    col_clues, row_clues = clues
    # Crear una matriz de 5x5 con todos los elementos inicializados en '_'
    matrix = [['_' for _ in range(5)] for _ in range(5)]
    # Fill in cells based on column clues
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
    # Fill in cells based on row clues
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
    # Use logical deduction to fill in remaining cells
    for row in range(5):
        for col in range(5):
            if matrix[row][col] == '_':
                matrix[row][col] = '1'
    return matrix

clues = ([2, 1], [1, 1, 1], [2, 1], [1, 1, 1], [2, 1]), ([1, 1], [2, 2], [3, 1], [2, 2], [1, 1])

solved_nonogram = solve_nonogram(clues)

for row in solved_nonogram:
    print(row)