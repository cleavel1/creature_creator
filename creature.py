from species import Species

class Creature:
    def __init__(self, name: str, age: int, species: Species):
        self.name = name
        self.age = age
        self.species = species

    def get_name(self) -> str:
        return self.name
    
    def get_age(self) -> int:
        return self.age
    
    def get_species(self) -> Species:
        return self.species

