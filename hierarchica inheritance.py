# Parent class
class Animal:
    def speak(self):
        print("Animal speaks")

# Child class 1
class Dog(Animal):
    def bark(self):
        print("Dog barks")

# Child class 2
class Cat(Animal):
    def meow(self):
        print("Cat meows")

# Create objects of Dog and Cat
dog = Dog()
cat = Cat()

# Access methods
dog.speak()  # From Animal
dog.bark()   # From Dog

cat.speak()  # From Animal
cat.meow()   # From Cat
