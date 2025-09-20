from data import dict_poudlard

def cast_spell(sorcier, sort):
    print(f"{sorcier} lance le sort {sort}")

def print_lecture(sorcier, cours):

    info = dict_poudlard[sorcier]
    match info:
        case {"statut": "eleve", "cours": list(cours_suivis)}:
            if cours in cours_suivis:
                print(f"{sorcier} est en train de suivre le cours de {cours}.")
            
            else:
                cours_suivis.append(cours)
                print(f"{sorcier} s'inscrit au cours de {cours}.")
        case {"statut": "professeur", "retired":False, "cours": list(cours_suivis)}:
            if cours in cours_suivis:
                print(f"{sorcier} enseigne le cours de {cours}.")
            
            else:
                print(f"{sorcier} n'est pas forme au cours de {cours}.")
