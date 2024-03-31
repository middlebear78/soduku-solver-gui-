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


    row, col = check_empty(board)
    if row is None:
        return True

    for guess in range(1, 10):
        if is_valid_num(board, guess, row, col):
            board[row][col] = guess
            if solve_sodoku(board):
                return True
        board[row][col] = 0

    return False

def is_valid_num(board, guess, row, col):

    board_row = board[row]
    board_column = [board[i][col] for i in range(len(board))]
    if guess in board_row or guess in board_column:
        return False

    row_start, column_start = (row // 3) * 3, col // 3 * 3

    for i in range(row_start, row_start+3):
        for j in range(column_start,column_start+3):
            if board[i][j] == guess:
                return False

    return True

def print_board(board):

    for i in range(len(board)):
        if i % 3 == 0 and i != 0:
            print("-- -- -- -- -- -- -- -- -")
        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0 :
                print(" | ", end=" ")

            if j == 8:
                print(board[i][j])
            else:
                print(board[i][j],end=" ")

# print_board(board)


def check_empty(board):

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == 0:
                return i, j
    return None, None

if __name__ == '__main__':

    print('Board before solving:')
    print('-----------------------------')
    print_board(board)
    print()
    print('Board after solving:')
    print('-----------------------------')
    print(solve_sodoku(board))
    print_board(board)