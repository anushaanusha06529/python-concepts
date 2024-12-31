# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class 1 inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Child class 2 inheriting from Animal
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Grandchild class inheriting from both Dog and Cat
class Pet(Dog, Cat):
    def friendly(self):
        print("Pet is friendly")

# Create an object of the Pet class
pet = Pet()

# Access methods
pet.speak()   # From Animal
pet.bark()    # From Dog
pet.meow()    # From Cat
pet.friendly()  # From Pet
