class Pet:
    PET_TYPES = ['dog', 'cat', 'rodent', 'bird', 'reptile', 'exotic']
    all = []

    def __init__(self, name, pet_type, owner=None):
        if pet_type not in Pet.PET_TYPES:
            raise Exception('invalid pet type')

        self.name = name
        self.pet_type = pet_type
        self.owner = owner
        Pet.all.append(self)
        
        if owner is not None:
            owner.add_pet(self)  


class Owner:
    def __init__(self, name):
        self.name = name
        self._pets = []  # List to store the owner's pets

    def pets(self):
        """Returns the list of the owner's pets."""
        return self._pets

    def add_pet(self, pet):
       pet.owner = self 
       self._pets.append(pet)
       
       
    def get_sorted_pets(self):  
        
        return sorted(self._pets, key=lambda pet: pet.name)
