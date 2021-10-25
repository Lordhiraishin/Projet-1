# coding utf-8

# Imports

# Variables

# Functions


from Fizzbuzz import FizzBuzz
from Map1 import Drawmap
from Player import Draw, Move
from CodeCesar import CodeCesar
from NombreMysterieux import NombreMysterieux


def main():

    Drawmap()
    Draw()
    Direction = input("Quelle direction voulez vous prendre")
    Move(Direction)
    # FizzBuzz()
    # CodeCesar()
    # NombreMysterieux()
    
   


# Code starts here
if __name__ == "__main__":
    main()