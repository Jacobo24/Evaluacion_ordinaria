from collections import deque

def convert_position(position):
    col = ord(position[0]) - ord('a')
    row = int(position[1]) - 1
    return row, col

def knight(start, end):
    start_pos = convert_position(start)
    end_pos = convert_position(end)
    
    board = [[-1 for _ in range(8)] for _ in range(8)]
    board[start_pos[0]][start_pos[1]] = 0
    
    q = deque([start_pos])
    moves = [(2, 1), (2, -1), (-2, 1), (-2, -1), (1, 2), (1, -2), (-1, 2), (-1, -2)]
    
    while q:
        curr_pos = q.popleft()
        for move in moves:
            new_pos = (curr_pos[0] + move[0], curr_pos[1] + move[1])
            if (0 <= new_pos[0] < 8) and (0 <= new_pos[1] < 8):
                if board[new_pos[0]][new_pos[1]] == -1:
                    board[new_pos[0]][new_pos[1]] = board[curr_pos[0]][curr_pos[1]] + 1
                    q.append(new_pos)
                    if new_pos == end_pos:
                        return board[new_pos[0]][new_pos[1]]
    return -1

print(knight("a3", "b5")) # should return 1