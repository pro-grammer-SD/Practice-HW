# Dog Breed

# Lesson 27: Object-Oriented Programming
# Write a program to create a dog class with one class variable and two instance variables, and display the details of dogs of two different breeds.

class Dog:
    animal = "Dog"  

    def __init__(self, breed, color):
        self.breed = breed  
        self.color = color  

    def display_details(self):
        print(f"Animal: {self.animal}, Breed: {self.breed}, Color: {self.color}")

dog1 = Dog("Labrador", "Golden")
dog2 = Dog("Beagle", "Brown & White")

dog1.display_details()
dog2.display_details()
