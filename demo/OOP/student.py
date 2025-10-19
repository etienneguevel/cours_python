class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

    def __str__(self):
        return f"{self.firstname} {self.lastname}"


class Student(Person):
    def __init__(self, firstname, lastname, university):
        super().__init__(firstname, lastname)
        self.university = university        
    
    def get_university(self):
        return self.university
    
Etienne = Student("Etienne", "Guevel", "Sorbonne Université")
print(Etienne.firstname, Etienne.lastname, "est étudiant à", Etienne.get_university())