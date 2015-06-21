#Prüft, ob ein Jahr ein Schaltjahr ist
def schaltjahr(jahr): #Bem.: ':' eröffnet "alles" (Schleifen, Funktionen, ...) [wie geschweifte Klammern in Java]
    if(jahr%400==0 or (jahr%4==0 and jahr%100!=0)):
        return 1
    else: return 0

#Bestimmt die Länge eines Monats
def monatslaenge(jahr,monat): #Übergaben "jahr", um Schaltjahre für Februar zu detektieren
    if(monat in [1,3,5,7,8,10,12]):
        return 31
    elif (monat in [4,6,9,11]): #=else if
        return 30
    elif(monat in [2] and schaltjahr(jahr)==1):
        return 29
    else: return 28  
    
#Bestimmt den Wochentag
#
# 0 - Sonntag, 1 - Montag, 2 - Dienstag, 3 - Mittwoch, 
# 4 - Donnerstag, 5 - Freitag, 6 - Samstag
def wochentag(jahr,monat,tag): 
    #"/" = mit Rest, "//" = ohne Rest, "%" = ohne Rest
    
    mkz  = [6,2,2,5,0,3,5,1,4,6,2,4] #Liste der Monatskennzahlen OHNE Schaltjahr
    mkzs = [5,1,2,5,0,3,5,1,4,6,2,4] #Liste der Monatskennzahlen MIT Schaltjahr
    
    c = jahr//100; #Anzahl der vergangenen Jahrhunderte
    j = jahr%100; # Jahreszahl innerhalb eines Jahrhunderts
    
    if (schaltjahr(jahr)==1): 
        k = mkzs[monat]
    else: 
        k = mkz[monat]
    #d = tag + k + j + j//4 - 2 * (c%4) 
    return (tag + k + j + j//4 - 2 * (c%4) )%7 

    #Python kennt keine Case-Switches > entweder "if" oder "options"
    #http://bytebaker.com/2008/11/03/switch-case-statement-in-python/
    
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
        result=[[3,os,'Ostersonntag']]
    else: result=[[4,(os-31),'Ostersonntag']]
    #print(result)
    
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
