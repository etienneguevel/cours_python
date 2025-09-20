# Ici une liste de tuples contenant des informations sur des villes, dont leurs coordonnees
list_coordinates = [
    ("Paris", "France", "Europe", "francais", (48.51, 2.21)),
    ("Tokyo", "Japon", (35.41, 139.41)),
    ("Buenos Aires", "Argentine", "Amerique", "espagnol", (-34.69, -58.22))
]

# *infos indique que les arguments positionnels mis 'en trop' seront captes
# sous forme de liste portant le nom infos.
# Par convention on nomme plutot infos '*args', mais on peut choisir le nom que l'on souhaite
def print_trivia(*infos):
    print(type(infos))
    print("information about this city:", ", ".join(infos))

for ville, *autres, (lon, lat) in list_coordinates:
    # On print les arguments deballes
    print(f"{ville}: {lon} | {lat}")
    # Tous les arguments mis en trop sont contenus dans la liste autres
    print(autres)
    # On 'unpack' autres dans la fonction print_trivia
    print_trivia(*autres)
    