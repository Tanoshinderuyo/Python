import random

class Crop:
	
	#Konstruktor
	def __init__(self, growth_rate, light_need, water_need):
		
		#Attribute
		self._growth = 0
		self._days_growing = 0
		self._growth_rate=growth_rate
		self._light_need=light_need
		self._water_need=water_need
		self._status="Seed"
		self._type="Generic"
	
	#Dictionary mit Water und Light - Needs
	def needs(self):
		return {'light need':self._light_need, 'water need':self._water_need}
	
	#Dictionary mit Current-State des Crop´s
	def report(self):
		return {'Type':self._type, 'Status':self._status, 'Growth':self._growth, 'Days Growing':self._days_growing}
	
	#Update Status 
	def _update_status(self):
		if self._growth > 15:
			self._status="Old"
		elif self._growth > 10:
			self._status = "Mature"
		elif self._growth > 5:
			self._status = "Young"
		elif self._growth > 0:
			self._status = "Seedling"
		elif self._growth == 0:
			self._status = "Seed"
		
	#Wachsen lassen
	def grow(self, light, water):
		if light >= self._light_need and water >= self._water_need:
			self._growth += self._growth_rate
		
		#Wachstumstage inkrementieren
		self._days_growing += 1
		#Status-Update
		self._update_status()
		
		
#Klassenunabhängige Funktion
def auto_grow(crop, days):
	for day in range (days):
		light = random.randint(1,10)
		water = random.randint(1,10)
		crop.grow(light, water)

	
#Manuell wachsen lassen
def manual_grow(crop):
	#eingabe-abfang
	valid = False
	while not valid:
		try:
			light = int(input("Please enter Light Value between 1-10: "))
			if 1 <= light <=10:
				valid=True
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
					valid=True
			else:
				print("No Valid Value, please enter between 1-10")
		except ValueError:
			print("No Valid Value, please enter between 1-10")
			
	#Values-gesetzt, Grow the Crop
	crop.grow(light, water)



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
	

def manage_crop(crop):
	print("This is the crop management program")
	print()
	noexit = True
	while noexit:
		display_menu()
		option = get_menu_choice()
		print()
		if option == 1:
			manual_grow(crop)
			print()
		elif option == 2:
			auto_grow(crop, 30)
			print()
		elif option == 3:
			print(crop.report())
			print()
		elif option == 0:
			noexit = False
			print()
	print("Thank you for using the crop management program")
	
	
def main():
	
	#Testinstanz anlegen
	new_crop=Crop(1,4,3)
	new_crop2=Crop(2,5,7)
	
	#testen
	#print(new_crop._status)
	#print(new_crop._light_need)
	#print(new_crop._water_need)
	
	#print(new_crop2._status)
	#print(new_crop2._light_need)
	#print(new_crop2._water_need)
	#print(new_crop.needs())
	#print(new_crop.report())
	#new_crop.grow(4,4)
	#auto_grow(new_crop, 20)
	#manual_grow(new_crop)
	#print(new_crop.report())
	manage_crop(new_crop)

if __name__ == "__main__":
	main()
	