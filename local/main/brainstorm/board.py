board = {}

def color(tile, color):
    try:
        if board[tile] != color:
            board[tile] = color
            led1 = tile*2
            led2 = tile*2+1

            print(f"{tile}: {color}")
    except:
        board[tile] = color
        led1 = tile*2
        led2 = tile*2+1

        print(f"{tile}: {color}")

