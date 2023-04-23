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
        if len(posibleCaptures) > 0:
            for posibleCapture in posibleCaptures:
                if posibleCapture[0] not in opponentPieces:
                    bestMoves.append(move)
        else:
            bestMoves.append(move)
    
    if len(bestMoves) == 0:
        bestMoves = possibleMoves

    return random.choice(bestMoves)