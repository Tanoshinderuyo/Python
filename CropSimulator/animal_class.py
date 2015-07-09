# -*- coding: utf-8 -*-
"""
Created on Sun Jul  5 11:14:09 2015

@author: admin
"""
import random

class Animal:
    
    #konstruktor
    def __init__(self, growth_rate, food_need, water_need):
        #Attribute
        self._weight = 0
        self._days_growing = 0
        self._growth_rate = growth_rate
        self._food_need = food_need
        self._water_need = water_need
        self._status = "Seed"
        self._type = "Generic"
        self._name = " "
        
        #Dictionary mit Food und Light - Needs
    def needs(self):
         return {'food need':self._food_need, 'water need':self._water_need}
	
	#Dictionary mit Current-State des Animal´s
    def report(self):
         return {'Type':self._type, 'Status':self._status, 'Weight':self._weight, 'Days Growing':self._days_growing, 'Name':self._name}
	
	#Update Status 
    def _update_status(self):
        if self._weight > 28:
            self._status = "Old"
        elif self._weight > 16:
            self._status = "Mature"
        elif self._weight > 7:
            self._status = "Young"
        elif self._weight > 0:
            self._status = "Freshling"
        elif self._weight == 0:
            self._status = "Newborn"
		
	#Wachsen lassen
    def grow(self, food, water):
        if food >= self._food_need and water >= self._water_need:
            self._weight += self._growth_rate
        
        #Wachstumstage inkrementieren
        self._days_growing += 1
        #Status-Update
        self._update_status()
        

#Klassenunabhängige Funktion
def auto_grow(animal, days):
	for day in range (days):
		food = random.randint(1,10)
		water = random.randint(1,10)
		animal.grow(food, water)

	
#Manuell wachsen lassen
def manual_grow(animal):
	#eingabe-abfang
	valid = False
	while not valid:
		try:
			food = int(input("Please enter Food Value between 1-10: "))
			if 1 <= food <=10:
				valid = True
			#DER ELSE ZWEIG HIER WIRD NIE VERWENDET, da Automatisch der ValueError abfängt
			else:
				print("No Valid Value, please enter between 1-10")
		except ValueError:
			print("No Valid Value, please enter between 1-10")
	
	valid = False
	while not valid:
		try:
			water = int(input("Please enter Water Value between 1-10: "))
			if 1 <= water <=10:
					valid = True
			else:
				print("No Valid Value, please enter between 1-10")
		except ValueError:
			print("No Valid Value, please enter between 1-10")
			
	#Values-gesetzt, Grow the Crop
	crop.grow(food, water)


#ALLGEMEIN NUR FÜR TESTZWECKE

def display_menu():
	print("1. Grow manually over 1 day")
	print("2. Grow automatically over 30 days")
	print("3. Report status")
	print("0. Exit test program")
	print()
	print("Please select an option from the above menu")
	

def get_menu_choice():
	option_valid = False
	while not option_valid:
		try:
			choice = int(input("Option Selected: "))
			if 0 <= choice <= 4:
				option_valid = True
			else:
				print("Please enter a valid option")
		except ValueError:
			print("Please enter a valid option")
	return choice
	

def manage_animal(animal):
	print("This is the animal management program")
	print()
	noexit = True
	while noexit:
		display_menu()
		option = get_menu_choice()
		print()
		if option == 1:
			manual_grow(animal)
			print()
		elif option == 2:
			auto_grow(animal, 30)
			print()
		elif option == 3:
			print(animal.report())
			print()
		elif option == 0:
			noexit = False
			print()
	print("Thank you for using the animal management program")