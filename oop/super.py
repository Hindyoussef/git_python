class Animal:
    def __init__(self, name):
        self.name = name

    def display(self):
        print(f"Animal Name: {self.name}")

class Sound:
    def make_sound(self):
        print("This animal makes a sound!")

class Dog(Animal, Sound):
    def __init__(self, name, breed):
        super().__init__(name)  # Calls __init__ of the first class in MRO
        self.breed = breed

    def display(self):
        super().display()  # Calls display method from the first class in MRO
        print(f"Breed: {self.breed}")

# Creating an object of Dog class
dog1 = Dog("Buddy", "Golden Retriever")
dog1.display()
dog1.make_sound()
print(Dog.mro())




