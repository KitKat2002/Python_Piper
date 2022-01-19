# Creates main class "pet"
class Pet:
    name = "Fido"
    species = "Canine"
    pID = "43"
#Parent class function
    def getPetInfo(self):
        pet_name = input("Enter your pet's name: ")
        pet_species = input("Enter your pet's species: ")
        pet_id = input("Enter your pet's id: ")
        if (pet_name == self.name and pet_id == self.pID):
            print("Hello, {}.".format(pet_name))
        else:
            print("Pet name or ID is incorrect.")
# Creates child class "Large_Pet"
class Large_Pet(Pet):
    weight = " "
    diet = " "
    temperment = " "
    brand = " "
#Child class function
    def getPetInfo(self):
        pet_name = input("Enter your pet's name: ")
        pet_species = input("Enter your pet's species: ")
        pet_brand = input("Enter your pet's brand: ")
        if (pet_name == self.name and pet_brand == self.brand):
            print("Hello, {}.".format(pet_name))
        else:
            print("Pet name or brand is incorrect.")


# Creates second child class "Pet_Diagnosis"
class Pet_Diagnosis(Pet):
    symptoms = " "
    duration_of_symptoms = " "
    last_location = " "
    illness = " "
#Second child class function
    def getPetInfo(self):
        pet_name = input("Enter your pet's name: ")
        pet_species = input("Enter your pet's species: ")
        pet_illness = input("Enter your pet's illness: ")
        if (pet_name == self.name and pet_illness == self.illness):
            print("Hello, {}.".format(pet_name))
        else:
            print("Pet name or illness is incorrect.")


