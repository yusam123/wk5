def create_board():
    board = []
    for i in range(9):
        board.append(0)
    return board
  

def win_check(board):
    diagonal_flag = 0
    diagonal_flag_r = 0
    draw_flag = 0
    for i in range(9):
        draw_flag = draw_flag * board[i]
    if draw_flag != 0:
        return 1
    for i in range(3):
        vertical_flag = 0
        horizontal_flag = 0
        for j in range(3):
            vertical_flag = vertical_flag + board[j + 3 * i]
            horizontal_flag = horizontal_flag + board[3 * j + i]
        diagonal_flag = diagonal_flag + board[i + 3 * i]
        diagonal_flag_r = diagonal_flag_r + board[6 - 2 * i]

        if vertical_flag == 6 or horizontal_flag == 6:
            return 2
        elif vertical_flag == 15 or horizontal_flag == 15:
            return 5
    if diagonal_flag == 6 or diagonal_flag_r == 6:
        return 2
    elif diagonal_flag == 15 or diagonal_flag_r == 15:
        return 5
    else:
        return 0      



