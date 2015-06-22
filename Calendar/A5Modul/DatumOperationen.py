""""#===== DATUM - DATENTYP - FUNKTIONEN =================================#"""

def toDate(eingabe):
	datum=[0,0,0]
	stringdatum=str(eingabe).split(".")
	for i in range(0, len(stringdatum),1):
		datum[i]=int(stringdatum[i])
	return datum
	
	
def dateToStr(datum):
	#Für die SUMMEN-Funktion
	a=str(datum[0])+'.'+str(datum[1])+'.'+str(datum[2])
	return a
	

	
""""#===== DATUM - OPERATIONEN - FUNKTIONEN ==============================#"""

def Abstand(a, b):
	datum1=toDate(a)
	datum2=toDate(b)
	anzahl=0
	if(LiegtVor(a,b)):
		if(datum1[2]!=datum2[2]):
			anzahl=TageImMonat(datum1[2],datum1[1])-datum1[0]
			for i in range (datum1[1]+1, 13, 1):
				anzahl+=TageImMonat(datum1[2], i)
			for j in range(datum1[2]+1, datum2[2],1):
				anzahl+=TageImJahr(j)
			for k in range(1, datum2[1],1):
				anzahl+=TageImMonat(datum2[2],k)
			anzahl+=datum2[0]
		elif(datum1[1]!=datum2[1]):
			anzahl=TageImMonat(datum1[2],datum1[1])-datum1[0]
			for i in range(datum1[1], datum2[1],1):
				anzahl+=TageImMonat(datum2[2],i)
			anzahl+=datum2[0]
		else:
			anzahl=datum2[0]-datum1[0]
	else:
		if(datum2[2]!=datum1[2]):
			anzahl=TageImMonat(datum2[2],datum2[1])-datum2[0]
			for i in range (datum2[1]+1, 13, 1):
				anzahl+=TageImMonat(datum2[2], i)
			for j in range(datum2[2]+1, datum1[2],1):
				anzahl+=TageImJahr(j)
			for k in range(1, datum1[1],1):
				anzahl+=TageImMonat(datum1[2],k)
			anzahl+=datum1[0]
		elif(datum2[1]!=datum1[1]):
			anzahl=TageImMonat(datum2[2],datum2[1])-datum2[0]
			for i in range(datum2[1], datum1[1],1):
				anzahl+=TageImMonat(datum1[2],i)
			anzahl+=datum1[0]
		else:
			anzahl=datum1[0]-datum2[0]
	return anzahl
		
	#//longint

""" 	Existenz-Funktion
	* Monat zwischen 1 und 12?
	* Tage in Range des Monats des Jahres?
	* Jahr darf negativ sein
	
	* Return Boolean"""	
def Existenz(a):
	datum=toDate(a)
	if(datum[1]>=1 and datum[1]<=12):
		if(datum[0]>=1 and datum[0]<=TageImMonat(datum[2],datum[1])):
			return True
	else:
		return False

		
def IstGleich(a, b):
	datum1=toDate(a)
	datum2=toDate(b)
	if(datum1[0]==datum2[0] and datum1[1]==datum2[1] and datum1[2]==datum2[2]):
		return True
	else:
		return False
		
	
def LiegtVor(a, b):
	#//Boolean
	datum1=toDate(a)
	datum2=toDate(b)
	if(datum1[2]<datum2[2]):
		return True
	elif(datum1[2]>datum2[2]):
		return False
	elif(datum1[1]<datum2[1]):
		return True
	elif(datum1[1]>datum2[1]):
		return False
	else:
		return datum1[0]<datum2[0]
	
def Vorgaenger(a):
	datum=toDate(a)
	vorgaenger=[0,0,0]
	#01.01.
	#monatsanfang
	if(datum[0]==1 and datum[1]==1):
		vorgaenger[0]=TageImMonat((datum[2]-1),12)
		vorgaenger[1]=12
		vorgaenger[2]=datum[2]-1
	elif(datum[0]==1 and datum[1]>1):
		vorgaenger[0]=TageImMonat(datum[2],(datum[1]-1))
		vorgaenger[1]=datum[1]-1
		vorgaenger[2]=datum[2]
	else:
		vorgaenger[0]=datum[0]-1
		vorgaenger[1]=datum[1]
		vorgaenger[2]=datum[2]
	return vorgaenger
	
def Nachfolger(a):
	datum=toDate(a)
	nachfolger=[0,0,0]
	if(datum[0]<TageImMonat(datum[2],datum[1])):
		nachfolger[2]=datum[2]
		nachfolger[1]=datum[1]
		nachfolger[0]=datum[0]+1
	elif (datum[1]<12):
		nachfolger[2]=datum[2]
		nachfolger[1]=datum[1]+1
		nachfolger[0]=1
	else:
		nachfolger[2]=datum[2]+1
		nachfolger[1]=1
		nachfolger[0]=1
	return nachfolger
	
	#//datum
	#//nicht Monatsletzter
	#//31. Dezember
	#//nicht 31. Dezember

	
#Prüft, ob ein Jahr ein Schaltjahr ist
def Schaltjahr(jahr): #Bem.: ':' eröffnet "alles" (Schleifen, Funktionen, ...) [wie geschweifte Klammern in Java]
    if(jahr%400==0 or (jahr%4==0 and jahr%100!=0)):
        return 1
    else: return 0

	
def Summe(a, anzahl):
	if(anzahl>0):
		for z in range (1, anzahl+1,1):
			#datum=Nachfolger(a)
			a=dateToStr(Nachfolger(a))
	elif(anzahl<0):
		for z in range(1, -anzahl+1,1):
			#datum=Vorgaenger(a)
			a=dateToStr(Vorgaenger(a))
	elif(anzahl==0):
		return toDate(a)
	ergebnis=toDate(a)
	#//ermittelt das #anzahl 
	#//folgende Datum anhand Nachfolger
	return ergebnis
	
def TageImMonat(jahr, monat):
    if(monat in [1,3,5,7,8,10,12]):
        return 31
    elif (monat in [4,6,9,11]): #=else if
        return 30
    elif(monat in [2] and schaltjahr(jahr)==1):
        return 29
    else: return 28 
	
def TageImJahr(jahr):
	if(schaltjahr(jahr)):
		return 366
	return 365
	
def Wochentag(a):
	datum=toDate(a)
	mkz  = [6,2,2,5,0,3,5,1,4,6,2,4]
	#Liste der Monatskennzahlen OHNE Schaltjahr
	mkzs = [5,1,2,5,0,3,5,1,4,6,2,4]
	#Liste der Monatskennzahlen MIT Schaltjahr
    
	c = int(datum[2])//100; 
	#Anzahl der vergangenen Jahrhunderte
	j = int(datum[2])%100; 
	#Jahreszahl innerhalb eines Jahrhunderts
    
	if (Schaltjahr(datum[2])==1): 
		k = mkzs[datum[1]-1]
	else: 
		k = mkz[datum[1]-1]
	d=(int(datum[0]) + k + j + j//4 - 2 * (c%4) )%7
	return d

	#//modimidofrsaso
	
def Ostersonntag(jahr):
	ostern=[0,0,jahr]
	k = jahr//100
	m = 15 + (3 * k + 3)//4 - (8 * k + 13)//25
	s = 2 - (3 * k + 3)//4
	a = jahr % 19
	d = (19 * a + m) % 30
	r = d // 29 + (d//28 - d//29) * (a//11)
	og = 21 + d -r
	sz = 7 - (jahr + jahr//4 + s) % 7
	oe = 7 - (og - sz) % 7
	os = og + oe
	if (os>=1 and os<=31):
		ostern[0]=os
		ostern[1]=3
		#result=[[3,os,'Ostersonntag']]
	else: 
		#result=[[4,(os-31),'Ostersonntag']]
		ostern[0]=os-31
		ostern[1]=4
	return ostern
	#Datum
	
#TESTUMGEBUNG=========================================================================#
def display_menu():
	print("1. Abstand")
	print("2. Existenz")
	print("3. IstGleich")
	print("4. LiegtVor")
	print("5. Vorgänger")
	print("6. Nachfolger")
	print("7. Schaltjahr")
	print("8. Summe - Nachfolger X")
	print("9. Tage im Monat")
	print("10. Tage im Jahr")
	print("11. Wochentag")
	print("12. Ostersonntag")
	print("0. Verlassen")
	print()
	print("Bitte wählen Sie eine Option")
	

def get_menu_choice():
	option_valid = False
	while not option_valid:
		try:
			choice = int(input("Gewählte Option: "))
			if 0 <= choice <= 12:
				option_valid = True
			else:
				print("Bitte einen gültigen Wert eingeben")
		except ValueError:
			print("Bitte einen gültigen Wert eingeben")
	return choice
	

def existant_input():
	option_valid = False
	while not option_valid:
		try:
			inputty = (input())
			count = 0
			punktcount = 0
			for char in inputty:
				if (ord(char) in [46,48,49,50,51,52,53,54,55,56,57]):
					if (ord(char)==46):
						punktcount += 1
					count += 1
				else:
					print("Bitte ein gültiges Datum eingeben")
			if (punktcount == 2 and (ord(inputty[(len(inputty)-1)])!= 46) and count == len(inputty) and Existenz(inputty)==True):
				option_valid = True
			else:
				raise ValueError
		except ValueError:
			print("Bitte ein gültiges Datum eingeben")
	return inputty
	

def manage_date():
	print("DatumOperationen - Testprogramm")
	print()
	noexit = True
	while noexit:
		display_menu()
		option = get_menu_choice()
		print()
		if option == 1:
			print("Geben Sie Datum a ein: ", end="")
			a = existant_input()
			print("Geben Sie Datum b ein: ", end="")
			b = existant_input()
			print(Abstand(a,b),"\n")
		elif option == 2:
			print("Geben Sie ein Datum ein: ", end="")
			a = existant_input()
			print(Existenz(a),"\n")
		elif option == 3:
			print("Geben Sie ein Datum a ein: ", end="")
			a = existant_input()
			print("Geben Sie ein Datum b ein: ", end="")
			b = existant_input()
			print(IstGleich(a,b),"\n")
		elif option == 4:
			print("Geben Sie ein Datum a ein: ", end="")
			a = existant_input()
			print("Geben Sie ein Datum b ein: ", end="")
			b = existant_input()
			print(LiegtVor(a,b),"\n")
		elif option == 5:
			print("Geben Sie ein Datum ein: ", end="")
			a = existant_input()
			print(dateToStr(Vorgaenger(a)),"\n")
		elif option == 6:
			print("Geben Sie ein Datum ein: ", end="")
			a = existant_input()
			print(dateToStr(Nachfolger(a)),"\n")
		elif option == 7:
			a = int(input("Geben Sie ein Jahr ein: "))
			print(Schaltjahr(a),"\n")
		elif option == 8:
			print("Geben Sie ein Datum a ein: ", end="")
			a = existant_input()
			b = int(input("Geben Sie eine Zahl ein: "))
			print(dateToStr(Summe(a,b)),"\n")
		elif option == 9:
			a = int(input("Geben Sie ein Jahr ein: "))
			b = int(input("Geben Sie einen Monat ein: "))
			print(TageImMonat(a,b),"\n")
		elif option == 10:
			a = int(input("Geben Sie ein Jahr ein: "))
			print(TageImJahr(a),"\n")
		elif option == 11:
			print("Geben Sie ein Datum ein: ", end="")
			a = existant_input()
			print(Wochentag(a),"\n")
		elif option == 12:
			a = int(input("Geben Sie ein Jahr ein: "))
			print(dateToStr(Ostersonntag(a)),"\n")
		elif option == 0:
			noexit = False
			print()
	print("Vielen Dank für die Benutzung der Testumgebung")
	
	
def main():
	

	manage_date()

if __name__ == "__main__":
	main()
	
