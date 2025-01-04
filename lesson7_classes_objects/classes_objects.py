class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        return f"{self.name} says woof!"

    def get_age(self):
        return self.age

# Creating an object of the Dog class
my_dog = Dog("Buddy", 3)

# Accessing object attributes and methods
print(my_dog.name)  # Output: Buddy
print(my_dog.get_age())  # Output: 3
print(my_dog.bark())  # Output: Buddy says woof!