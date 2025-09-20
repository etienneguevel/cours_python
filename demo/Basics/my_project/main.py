# Python possede des conventions pour le 'style' du code, notamment dans les imports
# On import d'abord ce qui vient des packages de base de python
from random import choice

# Puis ce aui vient de packages installes
from numpy import sqrt # Exemple, mais ici on ne l'utilise pas

# Et enfin les packages cree par l'utilisateur
# Quand dans une meme section il y a plusieurs import, on les classe par ordre alphabetique
from data import dict_poudlard, list_sorts
from utils import cast_spell, print_lecture


def main():
    sorcier = choice(list(dict_poudlard.keys()))
    spell = choice(list_sorts)
    cast_spell(sorcier, spell)
    print_lecture(sorcier, "potions")
    # Si l'eleve n'etait pas inscrit avant au cours de potion, il l'est maintenant
    print(dict_poudlard[sorcier])

if __name__ == "__main__":
    main()