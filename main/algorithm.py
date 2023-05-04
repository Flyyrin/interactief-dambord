"""
Bestand gebruikt om de ai logische stappen te laten nemen.
"""

# importeer nodioge modules en defineer alle basis variabelen
import random

# de functie getBestMove krijgt de class game mee als argument
# hij vraagt een lijst met mogelijke moves aan de game
# hij gaat de posities waar stukken van de tegenstander staan in een lijst zetten
# voor elke mogelijke move maakt hij een nieuw bord aan waar deze move is gemaakt,
# hij kijkt of hij hier nu niet geslagen kan worden en voegt deze move toe aan een lijstje
# hij geeft random een move van het lijstje met beste moves terug
# als de lijst met beste moves leeg is dan gebruikt hij de lijst met alle moelijke moves
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
    
    bestMove = random.choice(bestMoves)
    return bestMove