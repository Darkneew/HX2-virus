import sys
import random
player_2_ia = __import__(sys.argv[2]).ia
player_1_ia = __import__(sys.argv[1]).ia

def print_game (game):
    print("")
    for i in range(len(game["grid"])):
        print(" ".join(map(str, game["grid"][i])))
    print("")

def grid_generator (n, player_1, player_2):
    '''
    return a grid of size n, the player 1 and 2 arguments being their characters
    '''
    grid = []
    for i in range(n):
        row = []
        for j in range(n):
            row.append(0)
        grid.append(row)
    grid[0][0] = player_1
    grid[0][n-1] = player_2
    grid[n-1][0] = player_2
    grid[n-1][n-1] = player_1
    return grid

def random_move (game, side):
    '''
    Take the game object and the player's name (player_1 or player_2) and return a list [x, y] of a random valid move
    '''
    for i in range(len(game)):
        for j in range(len(game[i])):
            if valid_move(game, side, [i, j]):
                return [i, j]
    return False

def output (game):
    '''
    Take the game object and output the current game in a save file
    '''
    if game["player_1"]["start"]:
        filename = "./saves/" + game["player_1"]["name"] + "VS" + game["player_2"]["name"] + ".js"
    else :
        filename = "./saves/" + game["player_2"]["name"] + "VS" + game["player_1"]["name"] + ".js"
    f = open(filename, "w")
    f.write("const game = " + str(game["history"]) + ";")
    f.close()
    return True

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

def turn(game, player):
    '''
    The player play its turn in the game given
    '''
    move = game[player]["ia"](game, player)
    if not valid_move(game, player, move) or move == False:
        game["history"].append([player, False])
        return True
    game["grid"][move[0]][move[1]] = game["references"][player]
    game[player]["score"] += 1
    history_move = [player, [move[0], move[1], []]]
    for i in [-1, 0, 1]:
        if (move[0] + i) >= len(game["grid"]) or (move[0] + i) < 0:
            continue
        for j in [-1, 0, 1]:
            if (move[1] + j) >= len(game["grid"][i + move[0]]) or (move[1] + j) < 0:
                continue
            if game["grid"][move[0] + i][move[1] + j] != game["references"][player] and game["grid"][move[0] + i][move[1] + j] != game["references"]["neutral"]:
                game["grid"][move[0] + i][move[1] + j] = game["references"][player]
                history_move[1][2].append([move[0] + i, move[1] + j])
                game[player]["score"] += 2
                game["player_1"]["score"] -= 1
                game["player_2"]["score"] -= 1
    game["history"].append(history_move)
    return True

def play_game ():
    '''
    Make an actual game.
    '''
    Partie = {
        "player_1":{
            "start":bool(random.randint(0,1)),
            "name":sys.argv[1],
            "misc":{},
            "score":2,
            "ia": player_1_ia
        },
        "player_2":{
            "name":sys.argv[2],
            "misc":{},
            "score":2,
            "ia": player_2_ia
        },
        "grid": grid_generator(10, 1, 2),
        "references":{
            "player_1":1,
            "player_2":2,
            "neutral":0
        },
        "history":[]
    }
    if Partie["player_1"]["start"]:
        turn(Partie, "player_1")
    end = False
    while not end:
        turn(Partie, "player_2")
        turn(Partie, "player_1")
        if Partie["player_1"]["score"] + Partie["player_2"]["score"] == 100:
            end = True
    if Partie["player_1"]["score"] > Partie["player_2"]["score"]:
        print(Partie["player_1"]["name"] + " win")
    elif Partie["player_1"]["score"] < Partie["player_2"]["score"]:
        print(Partie["player_2"]["name"] + " win")
    else :
        print("egality")
    output(Partie)

play_game()