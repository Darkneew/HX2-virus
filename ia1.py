def valid_move(game, player, move):
    '''
    Determine if the move given [lign, column] is a valid move for the player in the game
    '''
    if move == False:
        return True
    if game["grid"][move[0]][move[1]] != game["references"]["neutral"]:
        return False
    for i in [-1, 0, 1]:
        if (move[0] + i) >= len(game["grid"]) or (move[0] + i) < 0:
            continue
        for j in [-1, 0, 1]:
            if (move[1] + j) >= len(game["grid"][i + move[0]]) or (move[1] + j) < 0:
                continue
            if game["grid"][move[0] + i][move[1] + j] == game["references"][player]:
                return True
    return False

def ia (game, side):
    best_pos = False
    best_score = -1
    for i in range(len(game["grid"])):
        for j in range(len(game["grid"][i])):
            if valid_move(game, side, [i, j]):
                score = 0
                for h in [-1, 0, 1]:
                    if (i + h) >= len(game["grid"]) or (i + h) < 0:
                        continue
                    for k in [-1, 0, 1]:
                        if (j + k) >= len(game["grid"][i + h]) or (j + k) < 0:
                            continue
                        if game["grid"][i + h][j + k] != game["references"]["neutral"] and game["grid"][i + h][j + k] != game["references"][side]:
                            score += 1
                if score > best_score:
                    best_pos = [i, j]
                    best_score = score
    return best_pos