from random import choice

# player wins the game:
combo_indices = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8],
    [0, 3, 6],
    [1, 4, 7],
    [2, 5, 8],
    [0, 4, 8],
    [2, 4, 6]
]

#The AI and the opponent player:

EMPTY_SIGN = '.'
AI_SIGN = 'X'
OPPONENT_SIGN = 'O'

#Intro to the game and directions:

print("****************WELCOME TO TIC TAC TOE FOOL**********************")
print("DIRECTION:")
print("The main goal of the game is to get three in a row")
print("To get three in a row you have to either get it horizontally, vertically or across")
print("To input the position you desire one must simply pic the row number and column number.")
print("*" * 15)
print("****************EXAMPLE BOARD***************************************")
print("****COLUMN******")
print("ROW #1: 1 | 2 | 3")
print("--------------------")
print("ROW #2: 4 | 5 | 6")
print("--------------------")
print("ROW #3: 7 | 8 | 9")
print("TIP: THINK OF BATTLESHIP YA KNOW THAT OG GAME YOU PLAYED AS A CHILD IF YOU WERE A 90'S KID")
print("*********************************************************************************************************")
print("")


#Prints and the board when the:
def print_board(board):
    #print("")
    #print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    #print('-' * 10)
    #print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    #print('-' * 10)
    #print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    #print("")
    print("")
    print(' | '.join(board[:3]))
    print('-' * 10)
    print(' | '.join(board[3:6]))
    print('-' * 10)
    print(' | '.join(board[6:]))
    print("")

#The movement of the player
#also generates the new board after every turn
def opponent_move(board, row, column):
    index = 3 * (row - 1) + (column - 1)
    if board[index] == EMPTY_SIGN:
        return board[:index] + OPPONENT_SIGN + board[index + 1:]
    return board


#
def all_moves_from_board(board, sign):
    move_list = []
    for i, v in enumerate(board):
        if v == EMPTY_SIGN:
            new_board = board[:i] + sign + board[i + 1:]
            move_list.append(new_board)
            if game_won_by(new_board) == AI_SIGN:
                return[new_board]
    return move_list


#Here is where the random move generates for the AI_player
def all_moves_from_board_list(board, sign):
    move_list = []
    for i, v in enumerate(board):
        if v == EMPTY_SIGN:
            move_list.append(board[:i] + sign + board[i + 1:])
            return move_list


def ai_move(board):
    new_boards = all_moves_from_board(board, AI_SIGN)
    for new_board in new_boards:
        if game_won_by(new_board) == AI_SIGN:
            print('won')
            return new_board
        return choice(new_boards)
    return choice(all_moves_from_board(board, AI_SIGN))


#determining who won the game
def game_won_by(board):
    for index in combo_indices:
        if board[index[0]] == board[index[1]] == board[index[2]] != EMPTY_SIGN:
            return board[index[0]]
        return EMPTY_SIGN


#The game loop
#Where all the magic happens
def game_loop():

    board = EMPTY_SIGN * 9
    empty_cell_count = 9
    is_game_ended = False
    while empty_cell_count > 0 and not is_game_ended:
        if empty_cell_count % 2 == 1:
            board = ai_move(board)
        else:
            #where the player would enter numbers or position of where they want to place there O
            row = int(input('ENTER ROW: '))
            col = int(input('ENTER COLUMN: '))
            board = opponent_move(board, row, col)
        print_board(board)
        is_game_ended = game_won_by(board) != EMPTY_SIGN
        empty_cell_count = sum(1 for cell in board if cell == EMPTY_SIGN)
    print('GAME HAS BEEN ENDED')


game_loop()
