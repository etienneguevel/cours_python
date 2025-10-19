from random import choice

class Sorcier:
    houses = ("griffondor", "serpentard", "poufsouffle", "serdaigle")
    def __init__(self, name, genre, hair, house=None):
        self._name = name
        if not house:
            
            self.house = self.choipeau()

        elif house not in self.houses:
            raise ValueError(f"{house} n'est pas une maison valide.")

        else:
            self.house = house
        
        self.genre = genre
        self.hair = hair

    @classmethod
    def choipeau(cls):
        h = choice(cls.houses)
        print(f"Le choipeau dit... {h}")

        return h

    def cast_spell(self, spell):
        print(f"{self.name.capitalize()} lance le sort {spell} !")

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        
        else:
            raise TypeError(f"{type(value)} n'est pas un nom.")
    

harry = Sorcier("harry", "homme", "noir")
harry.name = 'draco'

harry.name = 123