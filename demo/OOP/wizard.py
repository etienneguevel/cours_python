from random import choice

class Sorcerer:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if isinstance(value, str):
            self._name = value
        else:
            raise TypeError(f"{type(value)} n'est pas un nom.")
        
    def print_name(self):
        print(self.name)

class Student(Sorcerer):
    houses = ("griffondor", "serpentard", "poufsouffle", "serdaigle")
    def __init__(self, name, house=None):
        super().__init__(name)
        if not house:
            self.house = self.choipeau()

        elif house not in self.houses:
            raise ValueError(f"{house} n'est pas une maison valide.")

        else:
            self.house = house

    @classmethod
    def choipeau(cls):
        h = choice(cls.houses)
        print(f"Le choipeau dit... {h}")

        return h

class Teacher(Sorcerer, Student):
    def __init__(self, name, cours, house):
        super().__init__(name, house)
        self.cours = cours

    def print_name(self):
        print(f"M. ou Mme. {self.name.capitalize()}")

albus = Sorcerer("Albus")
harry = Student("Harry", "griffondor")
severus = Teacher("Severus", "potions")

print(albus.name)
harry.print_name()
severus.print_name()
