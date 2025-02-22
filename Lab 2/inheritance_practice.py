"""
Author: Kevin Avina-Gutierrez
Description: Practicing inheritance and 
    other OOP paradigms
Date: 02/22/2025
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
        # Protected variable for health
        self.__healthy = True
        pass 

    # Getter for the __healthy variable
    def get_healthy(self):
        return self.__healthy

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
        # Check if the animal is friendly
        if self.temperment == "friendly":
            print(f"{self.animal_name} is friendly!")
            return True
        # Add statements for various temperments if not friendly
        else:
            print(f"{self.animal_name} is not friendly... watch out!")
            return False

class Bird(Animal):

    # Define the bird's constructor
    def __init__(self, name):
        # Call the parent constructor
        super().__init__(name)
        # Keeps track of their eggs
        self.nest_location = None
    
    def fly(self):
        print("I can fly?")
    
    def speak(self):
        print("chirp chirp chirp")

    # Getter for the __healthy variable
    def get_healthy(self):
        return self.__healthy

class Fish(Animal):

    # Define the fish's constructor
    def __init__(self, name):
        # Call the parent constructor
        super().__init__(name+"fish")
        
    def swim(self):
        print("Just keep swimming")
    

def run():
    # Testing the Fish class
    an_animal = Fish("Clown")
    print(an_animal.animal_name)
    an_animal.swim()
    an_animal.speak()

    """
    # Testing the Animal class
    an_animal = Animal("Unknown")
    print(an_animal.get_healthy())
    """

    """
    # Initialize an animal
    an_animal = Animal("Alligator")
    # Make the animal speak
    an_animal.speak()
    # Make the animal sleep
    an_animal.sleep()
    # Make the animal eat
    an_animal.eat("carrot")

    # Initialize a bird
    a_bird = Bird("Big Bird")
    # Make the bird fly
    a_bird.fly()
    # Make the bird sleep
    a_bird.sleep()
    # Make the bird speak
    a_bird.speak()
    # Test our bird constructor
    print(a_bird.nest_location)
    """

if __name__ == "__main__":
    run()