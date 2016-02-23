# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:26:58 2015

@author: admin
"""

from animal_class import *

class Cow(Animal):
    """A lil Cow Animal """
    
    #constructor
    def __init__(self,name):
        #call the super/parent class constructor with default values for cows
        #growth rate = 1; food need = 3; water need = 6
        super().__init__(1,3,6,name)
        self._type = "Cow"

    #override the grow method -- the Cows like Food .. ^^
    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            if self._status == "Freshling" and food > self._food_need:
                self._weight += self._growth_rate * 1.5
            elif self._status == "Young" and food > self._food_need:
                self._weight += self._growth_rate * 1.25
            else:
                self._weight += self._growth_rate
        #increment the growing
        self._days_growing += 1
        #update the status
        self._update_status()