# README

---

Il est de notorité publique que les jeunes taupins de Louis Le Grand s'ennuient dans leurs temps libre. 
Ainsi, pour tuer le temps, je propose de faire une petite compétition d'intelligences artificielles, sur le jeu du virus.

---

## Le jeu du virus

Le jeu du virus est un jeu de plateau à informations complètes qui se joue sur une grille carrée de 10 par 10, et où le but du jeu est d'avoir plus de pion que l'adversaire sur le plateau à la fin du jeu.

Les règles sont assez simple : 
Au début du jeu, chaque joueur commence avec deux pions, situés aux coins opposés de la grille. 
A chaque tour, le joueur peut placer un pion sur une case adjacente à un de ses pions déjà en jeu. Ensuite, tout les pions adverses adjacents au pion placé changent de camps, et c'est la fin du tour. 
Les diagonales comptent comme adjacents. On ne peux pas créer de réactions en chaine en convertissant les pions de l'adversaire.
Si un joueur ne peut pas jouer, il ne joue pas.
La partie se finie lorsque la grille est remplie ou alors lorsque aucun joueur ne peut jouer.

---

## MISC

### C'est pour quand?

De maintenant à une semaine après la rentrée ou encore un peu après, en fonction de ce que vous préferez.

### Comment s'inscrire?

Envoyez moi un message privé pour signaler que vous participez, et quand votre IA est finie, envoyez la par message privé aussi

### Quel niveau de Python il faut pour faire une IA?

Franchement, il suffit de savoir faire des additions, des soustractions, et des if else. 

### Et à la fin?

Quand j'aurais reçu toute les IAs, je les ferais toute s'affronter, et celle qui battra le plus d'autres IAs gagnera. Je projetterais surement les matchs à la rentrée en VH141

---

## L'IA

Votre but est de créer un fichier `votre_nom.py` qui a une fonction appelée `ia` qui prendra deux arguments, le dictionnaire `game` et la chaine de charactère représentant votre côté, et qui retournera une liste de deux entiers qui representeront les deux coordonnées (ligne / colonne), ou False si l'IA ne peut/veut pas jouer.

Example :
```py
def ia (game, side):
    for i in range(len(game["grid"])):
        for j in range(len(game["grid"][i])): # parcours la grille 
            if game["grid"][i][j] != game["references"]["neutral"]: # vérifie que la case est libre
                continue
            for k in [-1, 0, 1]:
                if (i + k) >= len(game["grid"]) or (i + k) < 0:
                    continue
                for l in [-1, 0, 1]:
                    if (j + l) >= len(game["grid"][i + k]) or (j + l) < 0:
                        continue
                    if game["grid"][i + k][j + l] == game["references"][side]:
                        return [i, j] # Si il y a un pion de son camps adjacent, le coup est valide et il renvoie donc la position
    return False
```

##### Conditions :

Votre IA ne doit pas modifier l'argument qui lui est transmis
Si le coup que l'IA veut jouer est illegal, elle passera son tour
Votre IA ne doit pas prendre plus de 10 sec a jouer
Vous avez le droit de recopier les fonctions déjà écrites dans le code source

### Le dictionnaire game :
```py
game = {
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
```

#### game["player_1"] et game["player_2]

La propriété `start` n'existe que pour le `player_1`. C'est une valeur booléenne qui indique si ce joueur commence ou pas.

La propriété `name` est une chaine de charactère correspondant au vrai nom du codeur de l'ia

La propriété `misc` est un objet un peu à part. C'est la seule propriété que vous pouvez modifier dans le dictionnaire `game`. Ce dictionnaire est en effet là pour que vous puissiez stocker des variables permanentes au cours de la partie. Bien évidemment, vous ne pouvez modifier que le `misc` associé à votre camp.

La propriété `score` est un nombre entier comptant le nombre de case que vous avez.

La méthode `ia` est la fonction que vous devez créer.

#### game["grid"] et game["references]

La propriété `grid` est une liste de liste, représentant la grille de jeu. Chaque liste dans la liste représente une ligne. 
Ainsi, la ligne 4 de la colonne 7 est représentée par `game["grid"][6][3]`. Il ne faut pas oublier que les listes sont indexées de 0 à 9. La valeur de chaque case est un nombre, référencée dans `game["references"]`. 

Pour savoir comment est indiquée une case vide, allez dans `game["references"]["neutral"]`. Il en va de même pour les pions des deux joueurs, dans `player_1` et `player_2`

#### game["history"]

La propriété `history` du dictionnaire est simplement l'historique de la partie. Le premier élément est le premier coup joué, et ainsi de suite jusqu'au dernier élément, qui est donc le dernier coup de l'adversaire. 

Un coup est une liste de deux éléments, le premier élément étant le joueur qui l'a joué, le deuxième étant le coup en lui même. Le deuxième élément est aussi une liste, de trois éléments, les deux premiers étants les coordonnées du coup joué, le troisième élément étant à nouveau une liste. Cette liste est une liste de coordonnées (elles-mêmes représentées par des listes) des pions convertis par le coup joué. Si un joueur saute son tour, pour son coup, au lieu d'une liste, il y aura simplement `False`

```
```

> Si vous trouvez des exploits, bug, optimisations possibles, ou autre, merci de fork.
> Vous avez bien entendu le droit de tester vos IAs en avance ou même de vous entrainer entre vous.

## Liste des participants

 - Léo
 - Adam
