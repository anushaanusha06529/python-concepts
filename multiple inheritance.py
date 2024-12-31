# Parent class 1
class Animal:
    def speak(self):
        print("Animal speaks")

# Parent class 2
class Bird:
    def fly(self):
        print("Bird flies")

# Child class inheriting from both Animal and Bird
class Bat(Animal, Bird):
    def feature(self):
        print("Bat can both speak and fly")

# Create an object of the Bat class
bat = Bat()
bat.speak()  # From Animal
bat.fly()    # From Bird
bat.feature()  # From Bat
