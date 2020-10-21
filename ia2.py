def ia (game, side):
    for i in range(len(game["grid"])):
        for j in range(len(game["grid"][i])):
            if game["grid"][i][j] != game["references"]["neutral"]:
                continue
            for k in [-1, 0, 1]:
                if (i + k) >= len(game["grid"]) or (i + k) < 0:
                    continue
                for l in [-1, 0, 1]:
                    if (j + l) >= len(game["grid"][i + k]) or (j + l) < 0:
                        continue
                    if game["grid"][i + k][j + l] == game["references"][side]:
                        return [i, j]
    return False