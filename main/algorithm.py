import random

def getBestMove(game):
    possibleMoves = game.get_possible_moves()
    opponentPieces = []
    for piece in game.board.pieces:
        if game.whose_turn() == 2:
            if piece.player == 1:
                opponentPieces.append(piece.position)

        if game.whose_turn() == 1:
            if piece.player == 2:
                opponentPieces.append(piece.position)

    bestMoves = []
    for move in possibleMoves:
        posibleCaptures = game.board.create_new_board_from_move(move).get_possible_capture_moves()
        print(f"als {move} mogelijke captures: {posibleCaptures}")
        if len(posibleCaptures) > 0:
            for posibleCapture in posibleCaptures:
                if posibleCapture[0] not in opponentPieces:
                    print(f"mogelijke captures, maar NIET door de enemy als {move}: {posibleCapture}")
                    bestMoves.append(move)
        else:
            bestMoves.append(move)
    
    if len(bestMoves) == 0:
        bestMoves = possibleMoves
        print(f"geen beste move, kies random")
    
    bestMove = random.choice(bestMoves)
    print(f"beste moves zijn {bestMoves}, kies random {bestMove}")
    return bestMove

from checkers.game import Game
game = Game()

while True:
    getBestMove(game)
    move = input("move: ")
    move = eval(move)
    game.move(move)

    for piece in game.board.pieces:
        print(f"{piece.position}:{piece.player}")
         