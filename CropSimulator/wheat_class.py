# -*- coding: utf-8 -*-
"""
Created on Tue Jun 30 17:03:33 2015

@author: admin
"""
from crop_class import *

class Wheat(Crop):
    """A potato Crop"""
    
    #constructor
    def __init__(self):
        #call the super/parent class constructor with default values for potato
        #growth rate = 1; light need = 3; water need = 6
        super().__init__(1,3,6)
        self._type = "Wheat"
    
    #override the grow method -- the potato likes more water .. ^^
    def grow(self, light, water):
        if light >= self._light_need and water >= self._water_need:
            if self._status == "Seedling":
                self._growth += self._growth_rate * 1.5
            elif self._status == "Young":
                self._growth += self._growth_rate * 1.25
            elif self._status == "Old":
                self._growth += self._growth_rate / 2
            else:
                self._growth += self._growth_rate
        #increment the growing
        self._days_growing += 1
        #update the status
        self._update_status()