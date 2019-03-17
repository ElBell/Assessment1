class PetOwner:
    def __init__(self, name: str = "Cory", pets=None):
        if pets is None:
            self.pets = []
        else:
            self.pets = pets
        self.name = name
        self.set_as_owner()

    def set_as_owner(self):
        for pet in self.pets:
            pet.owner = self

    def add_pet(self, new_pet):
        new_pet.owner = self
        self.pets.append(new_pet)

    def remove_pet(self, pet):
        self.pets.remove(pet)

    def is_owner_of(self, pet):
        return pet.owner == self

    def youngest_age(self):
        return min(self.pets).age

    def oldest_age(self):
        return max(self.pets).age

    def average_age(self):
        age_sum = 0
        for pet in self.pets:
            age_sum += pet.age
        return age_sum/len(self.pets)
