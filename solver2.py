board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
]


def solve_sodoku(board):
    pass


def check_empty(row, col):
    pass


def is_valid(board, guess, row, col):
    board_row = board[row]
    board_column = [board[i][col] for i in range(len(board))]
    if guess in board_row or guess in board_column:
        return False

    row_start, column_start = (row // 3) * 3, col // 3 * 3
