def create_board(size):
    board = ""
    space = 1
    for x in range(0, size):
        for x in range(0, size):
            board += (str(space) + "\t")
            space += 1
        board += "\n"
    return board


def add_piece(piece, space, board):
    new_board = board.replace(str(space), piece)
    return new_board


def check_winner(board):
    rows = board.splitlines()
    for index, row in enumerate(rows):
        rows[index] = row.replace("\t", "")

    # First check see if won by rows
    for row in rows:
        winner = True
        for character in row:
            if (row[0] != character):
                winner = False
        if winner:
            return True

    # Now columns
    for column in range(0, len(rows[0])):
        winner = True
        for row in range(1, len(rows[0])):
            if rows[row][column] != rows[0][column]:
                winner = False
        if winner:
            return True

    # Now Diagnols
    winner = True
    for x in range(0, len(rows)):
        if (rows[0][0] != rows[x][x]):
            winner = False
    if winner:
        return True

    # Now reverse diagnols
    winner = True
    for x in range(0, len(rows)):
        if (rows[0][len(rows)-1] != rows[x][len(rows)-1-x]):
            winner = False
    if winner:
        return True


def check_full(board):
    board = board.replace("\n", "")
    board = board.replace("\t", "")

    for x in board:
        if x != "X" and x != "O":
            return False
    return True


winner = False
turn = "X"

print("How large would you like the board?")
size = int(input())
board = create_board(size)

while True:

    print(board)
    print(f"Player {turn} choose a space!")

    space = input()
    board = add_piece(turn, space, board)

    if check_winner(board):
        print(board)
        print(f"Player {turn} wins!\tWould you like to play again?")
        again = input()
        if again == "y":
            board = create_board(size)
            continue
        else:
            break

    if check_full(board):
        print(board)
        print("It's a draw!\tWould you like to play again? y/n")
        again = input()
        if again == "y":
            board = create_board(size)
            continue
        else:
            break

    if turn == "X":
        turn = "O"
    else:
        turn = "X"
