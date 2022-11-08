from logic import create_board,win_check

def show_board(board):
    for i in range(9):
        if i % 3 == 0:
            print("|", end = "")
        if board[i] == 0:
            print("_ _", end = "|")
        elif board[i] == 2:
            print("_O_", end = "|")    
        elif board[i] == 5:
            print("_X_", end = "|")   
        if (i + 1) % 3 == 0:
            print("\n")  

def draw_broad(board,player):
    position = input("enter a position: ")
    board[3 * (int(position[1]) - 1) + int(position[3]) - 1]  = player    #(1,2)
    show_board(board)
    print("----------------------------")
(2)
if __name__ == '__main__':
    board = create_board()
    winner = None
    while winner == None:
        print("TODO: take a turn!")
        show_board(board)
        print("player 1")
        draw_broad(board,2)
        if win_check(board) == 2:
            winner = 'O'  
            print(winner)
        if win_check(board) == 5:
            winner = 'X'  
            print(winner)
        if win_check(board) == 1:
            winner = 'Draw'  
            print(winner)
        print("player 2")
        draw_broad(board,5)
        if win_check(board) == 2:
            winner = 'O'  
            print(winner)
        if win_check(board) == 5:
            winner = 'X'  
            print(winner)
        if win_check(board) == 1:
            winner = 'Draw'  
            print(winner)
    