"""
Write a function that will solve a 9x9 Sudoku puzzle. The function will take one argument
consisting of the 2D puzzle array, with the value 0 representing an unknown square.
The Sudokus tested against your function will be "easy" (i.e. determinable; there will be
no need to assume and test possibilities on unknowns) and can be solved with a brute-force approach.
"""

import itertools

def sudoku(puzzle):
    """return the solved puzzle as a 2d array of 9 x 9"""

    for i in range(len(puzzle)):
        for j in range(len(puzzle)):
            # Find next not filled out square
            if puzzle[i][j] == 0:
                # Test all the numbers
                for num in range(1, 10):
                    copy_puzzle = [row[:] for row in puzzle]
                    copy_puzzle[i][j] = num
                    if check_sudoku(copy_puzzle):
                        # If this number works in this square so far
                        # then keep working with it and fill in next
                        solution = sudoku(copy_puzzle)
                        if solution is not None:
                            # only get here when all fields are filled in
                            return solution
                # No number worked so backtrack
                return None

    return puzzle

# Credit to StackOverflow for the checking.
def sudoku_ok(line):
    return (len(line) == 9 and sum(line) == sum(set(line)))

def check_sudoku(grid):
    bad_rows = [row for row in grid if not sudoku_ok(row)]
    grid = list(zip(*grid))
    bad_cols = [col for col in grid if not sudoku_ok(col)]
    squares = []
    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
          square = list(itertools.chain(*[row[j:j+3] for row in grid[i:i+3]]))
          squares.append(square)
    bad_squares = [square for square in squares if not sudoku_ok(square)]
    return not (bad_rows or bad_cols or bad_squares)
