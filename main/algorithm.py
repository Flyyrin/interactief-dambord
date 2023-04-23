def getBestMove(game):
    bestMoves = []    
    enemyPieces = []
    for piece in game.board.pieces:
        if game.whose_turn() == 2:
            if piece.player == 1:
                enemyPieces.append(piece.position)

        if game.whose_turn() == 1:
            if piece.player == 2:
                enemyPieces.append(piece.position)
                
    for move in game.get_possible_moves():
        move = move[1]
        for i in [3,-5,-4,4]:
            if move + i not in enemyPieces:
                bestMoves.append(move)
        
    return bestMoves


from checkers.game import Game
game = Game()
print(getBestMove(game))