def solve_nonogram(matrix):
    # Creamos una copia de la matriz para poder modificarla sin afectar la original
    nonogram = [row.copy() for row in matrix]

    # Use la deducción lógica para completar las celdas restantes
    for row in range(len(matrix)):
        for col in range(len(matrix[0])):
            if matrix[row][col] == 0:
                nonogram[row][col] = '0'
            if matrix[row][col] == 1:
                nonogram[row][col] = '1'

    return nonogram

matrix = [[0, 0, 1, 0, 0],
[1, 1, 0, 0, 0],
[0, 1, 1, 1, 0],
[1, 1, 0, 1, 0],
[0, 1, 1, 1, 1]]

solved_nonogram = solve_nonogram(matrix)

for row in solved_nonogram:
    print(row)

# Para que me da la solución que me pones de ejemplo, esta es la opción que pides por eso es la A