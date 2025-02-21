"""
Author: Kevin Avina-Gutierrez
Description: Practicing inheritance and 
    other OOP paradigms
Date: 02/20/2025
"""

# Class defining a generic animal
class Animal:
    def __init__(self, name, hungry = False, temperment = "unknown"):
        # Name of the animal
        self.animal_name = name
        # Boolean representing if the animal is hungry
        self.hungry = hungry
        # Temperment of the animal, is it friendly or not?
        self.temperment = temperment
        pass 

    # Print what the animal "says"
    def speak(self):
        print("Speaking! What do I say??")

    # Make the animal sleep
    def sleep(self):
        print(f"{self.animal_name} is sleeping...zzzZZZzzz")
        # Set animal hunger to True
        self.hungry = True

    # Make the animal eat
    def eat(self, food):
        # Check if animal is hungry
        if self.hungry == True:
            print(f"{self.animal_name} ate {food}!")
            # Set animal to not hungry, since it just ate
            self.hungry = False
            return True
        
        # Animal is not hungry, return false
        else:
            print(f"{self.animal_name} did not eat {food}...")

            return False
    
    # Is the animal friendly?
    def is_friendly(self):
        if self.temperment == "friendly":
            print(f"{self.animal_name} is friendly!")
            return True
        # Add statements for various temperments
        else:
            print(f"{self.animal_name} is not friendly... watch out!")
            return False

def run():
    # Initialize an animal
    an_animal = Animal("T-rex")
    # Make the animal speak
    an_animal.speak()
    # Make the animal sleep
    an_animal.sleep()
    # Make the animal eat
    an_animal.eat("a person")

if __name__ == "__main__":
    run()