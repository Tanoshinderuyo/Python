# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 17:29:36 2015

@author: admin
"""

from cow_class import *
from sheep_class import *
from potato_class import *
from wheat_class import *

class Field:
    #Simulation eines Feldes mit Tieren und Pflanzen

    #constructor
    def __init__(self, max_animals, max_crops):
        self._crops = []
        self._animals = []
        self._max_animals = max_animals
        self._max_crops = max_crops
        
    def plant_crop(self, crop):
        if len(self._crops) < self._max_crops:
            self._crops.append(crop)
            return True
        else:
            return False
            
    def add_animal(self, animal):
        if len(self._animals) < self._max_animals:
            self._animals.append(animal)
            return True
        else:
            return False
            
    def harvest_crop(self, position):
        return self._crops.pop(position)
        
    def remove_animal(self, position):
        return self._animals.pop(position)

def main():
    new_field = Field(5,2)
    print(new_field._crops)
    print(new_field._animals)
    print(new_field._max_animals)
    print(new_field._max_crops)
    new_field.plant_crop(Wheat())
    new_field.add_animal(Sheep("Shaun"))
    print(new_field._animals)
    print(new_field._crops)
    #da wir nur ein objekt in der liste haben können wir das erste removen
    new_field.harvest_crop(0)
    new_field.remove_animal(0)
    print(new_field._animals)
    print(new_field._crops)

if __name__ == "__main__":
    main()    