import DatumOperationen

""" 	schaltjahr-Funktion
	* Prüft bekanntermaßen auf Schaltjahr
	
	* Return Integer"""
def schaltjahr(jahr):
    if(jahr%400==0 or (jahr%4==0 and jahr%100!=0)):
        return 1
    else: return 0

""" 	monatslaenge-Funktion
	* Abgleich mit Arrays der 31-, 30-Tage-Monate
	* Abgleich mit Februar mit oder ohne Schaltjahr
	* Ohne Fehlerabfang wäre jeder andere Monat außerhalb 1-12 28-tägig
	
	* Return Integer"""
def monatslaenge(jahr,monat):
    if(monat in [1,3,5,7,8,10,12]):
        return 31
    elif (monat in [4,6,9,11]): #=else if
        return 30
    elif(monat in [2] and schaltjahr(jahr)==1):
        return 29
    else: return 28  
    
""" 	Wochentag-Funktion
	* Kalenderformel von Jacobsthal
	* Monatskennzahlen mit und ohne Schaltjahr
	* Formelberechnung auf Basis der Kennzahlen
	
	* Return Integer"""	
def wochentag(jahr,monat,tag): 
    
    mkz  = [6,2,2,5,0,3,5,1,4,6,2,4] #Liste der Monatskennzahlen OHNE Schaltjahr
    mkzs = [5,1,2,5,0,3,5,1,4,6,2,4] #Liste der Monatskennzahlen MIT Schaltjahr
    
    c = jahr//100; #Anzahl der vergangenen Jahrhunderte
    j = jahr%100; # Jahreszahl innerhalb eines Jahrhunderts
    
    if (schaltjahr(jahr)==1): 
        k = mkzs[monat-1]
    else: 
        k = mkz[monat-1]
    #d = tag + k + j + j//4 - 2 * (c%4) 
    return (tag + k + j + j//4 - 2 * (c%4) )%7 

""" 	feiertage-Funktion
	* Erzeugung eines Arrays der eingetragenen Feiertage
	* Bisher:
	*	Ostersonntag
	*	1.Mai
	*	Tag der deutschen Einheit
	*	Weihnachten
	*	Pfingsten - 49 Tage nach Ostern
	*	Himmelfahrt - 39 Tage nach Ostern
	
	*	Abschließendes Sortieren für Ausgabe
	
	* Return Array"""	  
def feiertage(jahr):
	#result = [[]] #Format = [monat,tag,Name]
    
	#Ostersonntag
	k = jahr//100;
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
		ostern = [os, 3, jahr]
		result=[[3,os,'Ostersonntag']]
	else: 
		ostern = [os-31, 4, jahr]
		result=[[4,(os-31),'Ostersonntag']]
    
	#Pfingsten 
	#Zugriff auf "ostern-Array"
	pfingsten = DatumOperationen.toDate(DatumOperationen.Summe(DatumOperationen.dateToStr(ostern), 49))
	result += [[pfingsten[1],pfingsten[0],'Pfingsten']]
	
	#Himmelfahrt 
	#Zugriff auf "ostern-Array"
	himmel = DatumOperationen.toDate(DatumOperationen.Summe(DatumOperationen.dateToStr(ostern), 39))
	result += [[himmel[1],himmel[0],'Himmelfahrt']]
    
    
    
	#Weihnachtsfeiertage
	result+=[[12,25,'1. Weihnachtsfeiertag'],[12,26,'2. Weihnachtsfeiertag']]
    
	#1. Mai
	result+=[[5,1,'1. Mai']]
    
	# Tag der dt. Einheit
	result+=[[10,3,'Tag der dt. Einheit']]
    
	#Sortieren der Feiertage mittels "Minimum-steigt-ab"-Methode
	for tripel in range(0,len(result),1):
		#Vergleich mit dem Rest, hintertauschen
		for tripelrest in range(tripel+1,len(result),1):
			if(result[tripelrest][0]<result[tripel][0] or result[tripelrest][0]==result[tripel][0] and result[tripelrest][1]<result[tripel][1]):
				helper=result[tripelrest]
				result[tripelrest]=result[tripel]
				result[tripel]=helper
	return result
