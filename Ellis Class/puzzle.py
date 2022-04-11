# Representing our puzzle state
# (must encode size, elements, position of blank)
board = [[1, 8, 2], [5, 3, 4], [7, 6, '_']]
blank_position = [2, 2]  # [row,col]


def printBoard():
    for i in range(len(board)):
        print(board[i])


def move_left():
    # check if move is possible on column of blank
    current_row = blank_position[0]
    current_col = blank_position[1]
    if current_col > 0:
        print("move possible")
        temp = board[current_row][current_col-1]
        board[current_row][current_col-1] = "_"
        board[current_row][current_col] = temp
        blank_position[1] = current_col-1
        printBoard()
    else:
        print("move not impossible")


def move_up():
    # check if move is possible on row of blank
    current_row = blank_position[0]
    current_col = blank_position[1]
    if blank_position[0] > 0:
        print("move possible")
        temp = board[current_row-1][current_col]
        board[current_row-1][current_col] = "_"
        board[current_row][current_col] = temp
        blank_position[0] = current_row-1
        printBoard()
    else:
        print("move not impossible")


def move_down():
    # check if move is possible on row of blank
    current_row = blank_position[0]
    current_col = blank_position[1]
    if blank_position[0] > 0:
        print("move possible")

        temp = board[current_row+1][current_col]
        board[current_row+1][current_col] = "_"
        board[current_row][current_col] = temp
        blank_position[0] = current_row+1
        printBoard()
    else:
        print("move not impossible")


def move_right():
    # check if move is possible on column of blank
    current_row = blank_position[0]
    current_col = blank_position[1]
    if blank_position[1] < 2:

        print("move possible")
        temp = board[current_row][current_col+1]
        board[current_row][current_col+1] = "_"
        board[current_row][current_col] = temp
        blank_position[1] = current_col+1
        printBoard()
    else:
        print("move not impossible")


move_up()
move_left()
move_right()
move_down()
move_up()
move_up()
