# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class inheriting from Animal
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Grandchild class inheriting from Dog
class Puppy(Dog):
    def weep(self):
        print("Puppy weeps")

# Create an object of the Puppy class
puppy = Puppy()

# Access methods
puppy.speak()  # From Animal
puppy.bark()   # From Dog
puppy.weep()   # From Puppy
