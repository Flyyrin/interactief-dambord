from checkers.game import Game
from boardFunctionsTest import readController

def displayBoard(game):
    new_board = {}
    for i in range(1,65):
                new_board[i] = " "
    for piece in game.board.pieces:
        new_board[piece.position*2] = piece.player


    b = new_board
    b[game.selected] = "c"
    b[game.highlighted] = "h"
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
    print(b)

def startGame():
    game = Game()
    player = game.whose_turn()
    game.selected = 0
    game.highlighted = 1
    while not game.is_over():
        controller = readController(game.whose_turn())
        if controller == "up":
            if (game.highlighted + 8) <= 64:
                game.highlighted += 8
        if controller == "down":
            if (game.highlighted - 8) >= 1:
                game.highlighted -= 8
        if controller == "left":
            if (game.highlighted + 1) <= 64 :
                game.highlighted += 1
        if controller == "right":
            if (game.highlighted - 1) >= 1:
                game.highlighted -= 1
        if controller == "press":
            if game.highlighted == game.selected:
                game.selected = 0
            else:
                game.selected = game.highlighted

        # if selected != 0:
        #     board[selected] = "c"
        # board[highlighted] = "h"

        displayBoard(game)

startGame()