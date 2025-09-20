dict_poudlard = {
    "harry": {
        "house": "griffondor",
        "genre": "homme",
        "hair": "noir",
        "statut": "eleve",
        "cours": ["potions", "botanique", "qwiddich", "defense contre les forces du mal"]
    },
    "hermione": {
        "house": "griffondor",
        "genre": "femme",
        "hair": "marron",
        "statut": "eleve",
        "cours": ["potions", "botanique", "defense contre les forces du mal"]
    },
    "ron": {
        "house": "griffondor",
        "genre": "homme",
        "hair": "roux",
        "statut": "eleve",
        "cours": ["potions", "botanique", "defense contre les forces du mal"]
    },    
    "draco": {
        "house": "serpentard",
        "genre": "homme",
        "hair": "blond",
        "statut": "eleve",
        "cours": ["potions", "qwiddich", "defense contre les forces du mal"]
    },
    "luna": {
        "house": "serdaigle",
        "genre": "femme",
        "hair": "blanc",
        "statut": "eleve",
        "cours": ["potions", "lecture", "defense contre les forces du mal"]
    },
}

# On souhaite rajouter des lignes dans notre dictionnaire, ou modifier la valeur
# de certaines cle : ici ron vient de se faire renvoyer, et n'a plus de maison et de cours !
dict_bis = {
    "severus": {
        "house": "sepentard",
        "genre": "homme",
        "hair": "noir",
        "statut": "professeur",
        "cours": ["potions", "defense contre les forces du mal"]
    },
    "ron": {
        "house": None,
        "genre": "homme",
        "hair": "roux",
        "statut": "eleve",
        "cours": []
    },
}

# Dans notre dictionnaire initiale
print("Valeurs initiales :")
print("severus : ", dict_poudlard.get("severus", "Personne inconnu"))
print("ron : ", dict_poudlard["ron"])

# On ajoute les valeurs
dict_poudlard.update(dict_bis)

print("\nResultats apres update :")
print("severus : ", dict_poudlard["severus"])
print("ron : ", dict_poudlard["ron"])

# On peut aussi enlever des cles avec la methode pop
dict_poudlard.pop("ron")
print("\nResultat apres pop ron :")
print("ron : ", dict_poudlard.get("ron", "Personne inconnu"))
