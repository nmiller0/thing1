
def enumerate_moves(x, y):

    potential_moves = []     # moves before clean up function

# ------------------------------------------------------------------------------
    # resolve pawn moves. 4 possible moves maximally
    if board[x][y] == "bPawn":

        potential_moves.append([[x+1], [y]])

        # if the pawn is in the second rank (has not moved)
        try:
            if board[x+2][y] == "" and x == 1 and board[x+1][y] == "":
                potential_moves.append([[x+2], [y]])
        except IndexError:
            pass

        try:
            if board[x+1][y+1][0] == "w":
                potential_moves.append([x+1], [y+1])
        except IndexError:
            pass

        try:
            if board[x+1][y-1][0] == "w":
                potential_moves.append([x+1], [y-1])
        except IndexError:
            pass

# ------------------------------------------------------------------------------

    # resolve knight moves. 8 possible moves maximally
    elif board[x][y] == "bKnight":

        potential_moves.append([[x+2], [y+1]])
        potential_moves.append([[x+2], [y-1]])
        potential_moves.append([[x+1], [y+2]])
        potential_moves.append([[x+1], [y+2]])
        potential_moves.append([[x-2], [y-1]])
        potential_moves.append([[x-2], [y+1]])
        potential_moves.append([[x-1], [y+2]])
        potential_moves.append([[x-1], [y-2]])

# ------------------------------------------------------------------------------

    elif board[x][y] == "bBishop":

        # down and right
        a = x + 1
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a+1][b+1][0] == "w":
                    potential_moves.append([[a+1], [b+1]])
            except IndexError:
                pass
            a += 1
            b += 1

        # down and left
        a = x + 1
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a+1][b-1][0] == "w":
                    potential_moves.append([[a+1], [b-1]])
            except IndexError:
                pass
            a += 1
            b -= 1

        # up and right
        a = x - 1
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a-1][b+1][0] == "w":
                    potential_moves.append([[a-1], [b+1]])
            except IndexError:
                pass
            a -= 1
            b += 1

        # up and left
        a = x - 1
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a-1][b-1][0] == "w":
                    potential_moves.append([[a-1], [b-1]])
            except IndexError:
                pass
            a -= 1
            b -= 1

# ------------------------------------------------------------------------------

    elif board[x][y] == "bRook":
        # down
        a = x + 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a+1][b][0] == "w":
                    potential_moves.append([[a+1], [b]])
            except IndexError:
                pass
            a += 1

        # left
        a = x
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a][b-1][0] == "w":
                    potential_moves.append([[a], [b-1]])
            except IndexError:
                pass
            b -= 1

        # up
        a = x - 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a-1][b][0] == "w":
                    potential_moves.append([[a-1], [b]])
            except IndexError:
                pass
            a -= 1

        # right
        a = x
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a][b+1][0] == "w":
                    potential_moves.append([[a], [b+1]])
            except IndexError:
                pass
            b += 1

# ------------------------------------------------------------------------------

    elif board[x][y] == "bQueen":
        # down and right
        a = x + 1
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a+1][b+1][0] == "w":
                    potential_moves.append([[a+1], [b+1]])
            except IndexError:
                pass
            a += 1
            b += 1

        # down and left
        a = x + 1
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a+1][b-1][0] == "w":
                    potential_moves.append([[a+1], [b-1]])
            except IndexError:
                pass
            a += 1
            b -= 1

        # up and right
        a = x - 1
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a-1][b+1][0] == "w":
                    potential_moves.append([[a-1], [b+1]])
            except IndexError:
                pass
            a -= 1
            b += 1

        # up and left
        a = x - 1
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a-1][b-1][0] == "w":
                    potential_moves.append([[a-1], [b-1]])
            except IndexError:
                pass
            a -= 1
            b -= 1

        # down
        a = x + 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a+1][b][0] == "w":
                    potential_moves.append([[a+1], [b]])
            except IndexError:
                pass
            a += 1

        # left
        a = x
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a][b-1][0] == "w":
                    potential_moves.append([[a], [b-1]])
            except IndexError:
                pass
            b -= 1

        # up
        a = x - 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a-1][b][0] == "w":
                    potential_moves.append([[a-1], [b]])
            except IndexError:
                pass
            a -= 1

        # right
        a = x
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            potential_moves.append([[a], [b]])
            try:
                if board[a][b+1][0] == "w":
                    potential_moves.append([[a], [b+1]])
            except IndexError:
                pass
            b += 1

# ------------------------------------------------------------------------------

    elif board[x][y] == "bKing":

        potential_moves.append([[x+1], [y]])
        potential_moves.append([[x+1], [y+1]])
        potential_moves.append([[x], [y+1]])
        potential_moves.append([[x-1], [y+1]])
        potential_moves.append([[x-1], [y]])
        potential_moves.append([[x-1], [y-1]])
        potential_moves.append([[x], [y-1]])
        potential_moves.append([[x+1], [y-1]])

# ------------------------------------------------------------------------------

    moves = append_strip_negatives(potential_moves)
    return moves
