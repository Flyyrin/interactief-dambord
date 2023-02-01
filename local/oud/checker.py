from checkers.game import Game
from boardFunctionsTest import readController, updateLedBoard, chunks
# https://pypi.org/project/imparaai-checkers/

def intersperse(lst, item):
    result = [item] * (len(lst) * 2 - 1)
    result[0::2] = lst
    return result

def displayBoard(board):
    b = board
    print(f"""
        {b[64]} {b[63]} {b[62]} {b[61]} {b[60]} {b[59]} {b[58]} {b[57]} 
        {b[56]} {b[55]} {b[54]} {b[53]} {b[52]} {b[51]} {b[50]} {b[49]} 
        {b[48]} {b[47]} {b[46]} {b[45]} {b[44]} {b[43]} {b[42]} {b[41]} 
        {b[40]} {b[39]} {b[38]} {b[37]} {b[36]} {b[35]} {b[34]} {b[33]} 
        {b[32]} {b[31]} {b[30]} {b[29]} {b[28]} {b[27]} {b[26]} {b[25]} 
        {b[24]} {b[23]} {b[22]} {b[21]} {b[20]} {b[19]} {b[18]} {b[17]} 
        {b[16]} {b[15]} {b[14]} {b[13]} {b[12]} {b[11]} {b[10]} {b[9]} 
        {b[8]} {b[7]} {b[6]} {b[5]} {b[4]} {b[3]} {b[2]} {b[1]}
        """)
    

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
    for index, row in enumerate(board_list):
        new_row = intersperse(row, ' ')
        if (index % 2) == 0:
            new_row.append(" ")
        else:
            new_row.insert(0, " ")
        new_board_list.append(new_row)
    

    # new_new_board_list = []
    # for index, row in enumerate(new_board_list):
    #     if (index % 2) == 0:
    #         row.reverse()
    #     new_new_board_list.append(row)

    llist = []
    for row in new_board_list:
        llist += row
    
    ddict = {}
    for position, player in enumerate(llist):
        ddict[position+1] = player
    return ddict

def shrinkBoard(gameboard):
    board = []
    for player in gameboard.values():
        board.append(player)
    
    gameboard = []
    for i in range(0, len(board), 8):
        gameboard.append(board[i : i+8])

    # reversedBoard = []
    # for index, row in enumerate(gameboard):
    #     if (index % 2) == 0:
    #         row.reverse()
    #     reversedBoard.append(row)
    
    shrunkList = []
    for row in reversedBoard:
        shrunkList.append(row[::2])

    llist = []
    for row in shrunkList:
        llist += row
        
    ddict = {}
    for position, player in enumerate(llist):
        ddict[position+1] = player

    keys = [k for k, v in ddict.items() if v == 'h']
    pos = keys

    return pos

def startGame():
    game = Game()
    game.test = "tests"
    player = game.whose_turn()
    selected = 0
    highlighted = 1
    while not game.is_over():
        controller = readController(game.whose_turn())
        if controller == "up":
            if (highlighted + 8) <= 64:
                highlighted += 8
        if controller == "down":
            if (highlighted - 8) >= 1:
                highlighted -= 8
        if controller == "left":
            if (highlighted + 1) <= 64 :
                highlighted += 1
        if controller == "right":
            if (highlighted - 1) >= 1:
                highlighted -= 1
        if controller == "press":
            print(game.test)
            if highlighted == selected:
                selected = 0
            else:
                selected = highlighted

        print(f"highlighted = {highlighted}")
        print(f"selected = {selected}")
      
        board = extendBoardVisualDict(game.board)

        if selected != 0:
            board[selected] = "c"
        board[highlighted] = "h"

        print(shrinkBoard(board))

        displayBoard(board)

startGame()