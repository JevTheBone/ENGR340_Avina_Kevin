"""
Author: Kevin Avina-Gutierrez
Description: Practicing inheritance and 
    other OOP paradigms
Date: 02/14/2025
"""

# Class defining a generic animal
class Animal:
    def __init__(self, name, hungry, temperment):
        # Name of the animal
        animal_name = name
        # Boolean representing if the animal is hungry
        hungry = False
        # Temperment of the animal
        animal_temperment = temperment
        pass 

    # Print what the animal "says"
    def speak(self):
        print("Speaking! What do I say??")

    # Make the animal sleep
    def sleep(self):
        print("{animal_name} is sleeping...zzzZZZzzz")

def run():
    # Initialize an animal
    an_animal = Animal()
    # Make the animal speak
    an_animal.speak()

if __name__ == "__main__":
    run()