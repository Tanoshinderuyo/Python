# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:27:12 2015

@author: admin
"""

from animal_class import *

class Sheep(Animal):
    """A lil Cow Animal """
    
    #constructor
    def __init__(self):
        #call the super/parent class constructor with default values for cows
        #growth rate = 1; food need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Sheep"

    #override the grow method -- the Sheep likes more water than food ofc .. ^^
    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Freshling" and water > self._water_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "Young" and water > self._water_need:
                self._weight += self._growth_rate * 1.25
            else:
                self._weight += self._growth_rate
        #increment the growing
        self._days_growing += 1
        #update the status
        self._update_status()