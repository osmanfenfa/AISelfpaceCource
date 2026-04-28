# THANKS TO INVENT WITH PYTHON: AUTOMATE THE BORING STUFF

def white_rook_can_capture(rook, board):
    captures = []
    rook_file = rook[0]   # column (letter)
    rook_rank = rook[1]   # row (number)

    for square, piece in board.items():
        file = square[0]
        rank = square[1]
        if piece[0] == 'b':
            if file == rook_file or rank == rook_rank:
                captures.append(square)
    return captures

board = {
    'd7': 'bQ',
    'd2': 'wB',
    'f1': 'bP',
    'a3': 'bN'
}

result = white_rook_can_capture('d3', board)
print(result)