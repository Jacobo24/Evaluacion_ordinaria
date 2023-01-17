class Nonogram:
    def _init_(self, clues):
        self.row_clues, self.col_clues = clues
        self.row_len, self.col_len = len(self.row_clues), len(self.col_clues)
        self.puzzle = [[0 for _ in range(self.col_len)] for _ in range(self.row_len)]
        
    def solve(self):
        # Use backtracking algorithm to solve the nonogram
        self._solve(0, 0)
        return self.puzzle
    
    def _solve(self, row, col):
        # Base case: if we have filled the entire puzzle, return true
        if row == self.row_len and col == 0:
            return True
        
        # Move to the next column if we have filled the current one
        if col == self.col_len:
            row += 1
            col = 0
        
        # Skip cells that have been filled
        if self.puzzle[row][col] != 0:
            return self._solve(row, col + 1)
        
        # Try filling the current cell with black and white, and move forward if valid
        for fill in (1, 0):
            self.puzzle[row][col] = fill
            if self._is_valid(row, col) and self._solve(row, col + 1):
                return True
        
        # Backtrack
        self.puzzle[row][col] = 0
        return False
    
    def _is_valid(self, row, col):
        # Check if the current row and col is valid based on the clues
        pass

if __name__ == "__main__":
    clues = ([[1], [2], [1]], [[1], [1], [1]])
    nono = Nonogram(clues)
    puzzle = nono.solve()
    print(puzzle)