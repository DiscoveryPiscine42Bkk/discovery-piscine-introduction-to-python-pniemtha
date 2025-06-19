def checkmate(board_string):
    board = board_string.strip().split('\n')
    size = len(board)

    king_pos = None
    for row in range(size):
        for col in range(len(board[row])):
            if board[row][col] == 'K':
                king_pos = (row, col)
                break
        if king_pos:
            break

    if king_pos is None:
        print("Fail")
        return

    king_row, king_col = king_pos

    for dx, dy in [(-1, -1), (-1, 1)]:
        x, y = king_row + dx, king_col + dy
        if 0 <= x < size and 0 <= y < len(board[x]):
            if board[x][y] == 'P':
                print("Success")
                return

    directions = {
        'R': [(0, 1), (0, -1), (1, 0), (-1, 0)],
        'B': [(1, 1), (-1, 1), (1, -1), (-1, -1)],
        'Q': [
            (0, 1), (0, -1), (1, 0), (-1, 0),
            (1, 1), (-1, 1), (1, -1), (-1, -1)
        ],
    }

    for piece, dirs in directions.items():
        for dx, dy in dirs:
            x, y = king_row + dx, king_col + dy
            while 0 <= x < size and 0 <= y < len(board[x]):
                current = board[x][y]
                if current == '.':
                    x += dx
                    y += dy
                    continue
                if current == piece or (piece == 'Q' and current in 'RBQ'):
                    print("Success")
                    return
                break

    print("Fail")
    