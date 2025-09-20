# La premiere situation est un exemple ou l'on va creer un probleme
wrong_grid = [["_"] * 3] * 3

# Cela equivaut a :
wrong_grid_bis = []
line = ["_"] * 3
for _ in range(3):
    wrong_grid_bis.append(line) # line est toujours le meme object !

# Ainsi quand on veut modifier un _ d'une ligne on modifie toutes les lignes
wrong_grid[1][1] = "X"
for line in wrong_grid:
    print(line)

# La deuxieme situation ne comporte pas ce probleme
correct_grid = [["_"] * 3 for _ in range(3)]

# Cette situation equivant a :
correct_grid_bis = []
for _ in range(3):
    line = ["_"] * 3
    print(id(line)) # line est a chaque fois un object different
    correct_grid_bis.append(line)

# Quand on modifie un element on ne rencontre plus le meme probleme
correct_grid[1][1] = "X"
for line in correct_grid:
    print(line)
