""" 
Author: Kevin Avina-Gutierrez
This is a test file for inheritance.py 
    It tests the Animal class and its methods
Date: 02/22/2025
"""

import pytest
from inheritance_practice import Animal

###########################################################
# To run the test you must use the command:               #
#   py -m pytest -v inheritance_tests.py(check directory) #
#   py -m pytest -v -m "method"_test inheritance_tests.py #
###########################################################

    ##########################
    # Tests for eat() method #
    ##########################

@pytest.mark.eat_tests
# Test if the animal ate
def test_eat():
    # Initialize an animal
    an_animal = Animal("Dog", True, "friendly")
    # Make the animal eat
    an_animal.eat("dog food")
    # Check that the animal is no longer hungry
    assert an_animal.hungry == False

@pytest.mark.eat_tests    
# Test if the animal didn't eat
def test_not_eat():
    # Initialize an animal
    an_animal = Animal("Dog", False, "friendly")
    # Make the animal eat
    result = an_animal.eat("dog food")
    # Check if the eat method returned False
    assert result == False

    ##########################
    # End of tests for eat() #
    ##########################
    
    ##################################
    # Tests for is_friendly() method #
    ##################################

@pytest.mark.is_friendly_tests
# Test if the animal is friendly
def test_is_friendly():
    # Initialize an animal
    an_animal = Animal("Dog", True, "friendly")
    # Check if the animal is friendly
    result = an_animal.is_friendly()
    # Check if the is_friendly method returned True
    assert result == True

@pytest.mark.is_friendly_tests
# Test if the animal is not friendly
def test_not_friendly():
    # Initialize an animal
    an_animal = Animal("Dog", True, "upset")
    # Check if the animal is friendly
    result = an_animal.is_friendly()
    # Check if the is_friendly method returned False
    assert result == False

    ######################################
    # End tests for is_friendly() method #
    ######################################

    ##############################
    # Tests for  method          #
    ##############################