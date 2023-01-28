
def color(tile, color):
    board[tile] = color

def refresh():
    for tile, color in board.items():
        try:
            if board[tile] != color:
                board[tile] = color
                led1 = tile*2
                led2 = tile*2+1

        except:
            board[tile] = color
            led1 = tile*2
            led2 = tile*2+1
            print(f"{tile}: {color}")