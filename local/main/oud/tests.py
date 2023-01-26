from checkers.game import Game

def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

def extendBoardVisual(gameboard):
    board = {}
    for i in range(1, 33):
            board[i] = " "
    for piece in gameboard.pieces:
        board[piece.position] = str(piece.player)

    positions = list(board.values())
    row1 = positions[0:4]
    row2 = positions[4:8]
    row3 = positions[8:12]
    row4 = positions[12:16]
    row5 = positions[16:20]
    row6 = positions[20:24]
    row7 = positions[24:28]
    row8 = positions[28:32]

    board_list = []
    board_list.append(row1)
    board_list.append(row2)
    board_list.append(row3)
    board_list.append(row4)
    board_list.append(row5)
    board_list.append(row6)
    board_list.append(row7)
    board_list.append(row8)

    new_board_list = []
    for row in board_list:
        new_row = intersperse(row, ' ')
        new_row.append(" ")
        new_board_list.append(new_row)

    new_new_board_list = []
    for index, row in enumerate(new_board_list):
        if (index % 2) == 0:
            row.reverse()
        new_new_board_list.append(row)

    return new_new_board_list

def extendBoardVisualDict(gameboard):
    board = {}
    for i in range(1, 33):
            board[i] = " "
    for piece in gameboard.pieces:
        board[piece.position] = str(piece.player)

    positions = list(board.values())
    row1 = positions[0:4]
    row2 = positions[4:8]
    row3 = positions[8:12]
    row4 = positions[12:16]
    row5 = positions[16:20]
    row6 = positions[20:24]
    row7 = positions[24:28]
    row8 = positions[28:32]

    board_list = []
    board_list.append(row1)
    board_list.append(row2)
    board_list.append(row3)
    board_list.append(row4)
    board_list.append(row5)
    board_list.append(row6)
    board_list.append(row7)
    board_list.append(row8)

    new_board_list = []
    for row in board_list:
        new_row = intersperse(row, ' ')
        new_row.append(" ")
        new_board_list.append(new_row)

    new_new_board_list = []
    for index, row in enumerate(new_board_list):
        if (index % 2) == 0:
            row.reverse()
        new_new_board_list.append(row)

    llist = []
    for row in new_new_board_list:
        llist += row
    
    ddict = {}
    for position, player in enumerate(llist):
        ddict[position+1] = player
    return ddict

def shrinkBoard(gameboard):
    reversedBoard = []
    for index, row in enumerate(gameboard):
        if (index % 2) == 0:
            row.reverse()
        reversedBoard.append(row)
    
    shrunkList = []
    for row in reversedBoard:
        shrunkList.append(row[::2])

    longList = []
    for row in shrunkList:
        longList += row
    
    shrunkBoard = {}
    for index, player in enumerate(longList):
        shrunkBoard[index + 1] = player
    
    return shrunkBoard

game = Game()

board = {}
for piece in game.board.pieces:
    board[piece.position] = str(piece.player)
print(board)

board = extendBoardVisual(game.board)


print("-"*10 + " Visual Code " + "-"*10)
for row in board:
    print(row)

print("-"*10 + " Code to add highlight to" + "-"*10)
print(extendBoardVisualDict(game.board))

board = shrinkBoard(board)

print("-"*10 + " Shrunk Code " + "-"*10)

print(board)