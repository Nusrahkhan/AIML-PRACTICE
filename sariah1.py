import random 

class Pet:
    def __init__(self, name, species, age):
        self.name = name
        self.species = species
        self.age = age

    def display_info(self):
        print(f"Name : {self.name}")
        print(f"Species: {self.species}")
        print(f"Age: {self.age}")

class Dog(Pet):
    def __init__(self, name, age, breed, color):
        super().__init__(name, "Dog", age)
        self.breed = breed
        self.color = color

    def display_info(self):
        super().display_info()
        print(f"Breed: {self.breed}")
        print(f"Color: {self.color}")

petStore = {}

#Generating random pet id's
def generate_id(existing_ids):
    while True:
        pet_id = random.randrange(10, 100)
        if pet_id not in existing_ids:
            return pet_id

# Adding a pet
def add_pet(name, species, age):
    pet_id = generate_id(petStore.keys())
    pet = Pet(name, species, age) #creating a pet object
    petStore[pet_id] = pet # adding object(pet) to dictionary(petStore) 
    return pet_id

#adding dog
def add_dog(name, age, breed, color):
    pet_id = generate_id(petStore.keys())
    dog = Dog(name, age, breed, color)
    petStore[pet_id] = dog
    return pet_id

# This is used to get the 
def get_pet(pet_id):
    return petStore.get(pet_id)

# displaying all pets in pet store
def viewPets():
    if not petStore:
        print("No pets in pet store.><")
    else:
        for pet_id, pet in petStore.items():
            print("**************")
            print(f"Pet ID: {pet_id}")
            pet.display_info()

def main():
    while True:
        print("\nPet Store Management System")
        print("1. Add Pet")
        print("2. Add dog")
        print("3. Adopt a Pet")
        print("4. View all pets")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter pet name: ")
            species = input("Enter pet species: ")
            age = int(input("Enter pet age: "))
            pet_id = add_pet(name, species, age)
            print(f"Pet added with ID: {pet_id}")

        elif choice == "2":
            name = input("Enter dog name: ")
            age = int(input("Enter dog age: "))
            breed = input("Enter breed: ")
            color = input("Enter color of dog: ")
            pet_id = add_dog(name, age, breed, color)
            print(f"Pet added with ID: {pet_id}")

        elif choice == "3":
          try:
            pet_id = int(input("Enter pet ID: "))
            pet = get_pet(pet_id)
            if pet:
              pet.display_info()
              print(f"Congrats on adopting {pet.name}")
              petStore.pop(pet_id)
            else:
              print("Pet not found")
          except ValueError:
            print("Invalid ID. Enter a number")

        elif choice == "4":
            viewPets()

        elif choice == "5":
            print("Thank you for visiting this store")
            break
        else:
            print("Invalid choice. Please try again.")
  
if __name__ == "__main__":
    main()