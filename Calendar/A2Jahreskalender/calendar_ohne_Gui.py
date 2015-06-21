import calfunctions

#Main-File
#verwendet: schaltjahr(jahr), monatslaenge(jahr,monat), wochentag(jahr,monat,tag)
def kalender(jahr):

    #Listen für schnellen Zugrif auf Monatsname und Wochentag
    monatsname = ['Januar','Februar','März','April','Mai','Juni','Juli','August','September','Oktober','November','Dezember']
    tagnamelang = ['Sonntag','Montag','Dienstag','Mittwoch','Donnerstag','Freitag','Samstag']
    tagname = ['So','Mo','Di','Mi','Do','Fr','Sa']
    
    
     #============================================
     # Erzeugung Tabelle
     #============================================
    
    for monat in range(0,12,1): #range(<Start>,<Ende>,>Schritt>) > Endwerte, die genau getroffen werden, werden nicht ausgegeben
        #header Monatsname + Tagliste
        print(monatsname[monat]) #default: print(monatsname[monat],end='\n') 
        for tag in range(1,8,1):
            print(tagname[tag%7],end='\t')#if the Buffer doesn't work, add: ",flush=True"
        print(end='\n')
        monatlang=calfunctions.monatslaenge(jahr,monat+1)

        
    #============================================
    #	Einträge in Tabelle
    #============================================     
        w = calfunctions.wochentag(jahr,monat,1)
            #fügt Leerzeichen ein vor erstem Eintrag in Monat
        if (w!=1):
            if(w!=0):
                print('\t'*(w-1)+'1',end='')
            else:
                print('\t'*6+'1',end='\n') #gibt 6* '\t' aus
        else: print(str(1),end='')   
            
        #schreibt die konsekutiven Wochentage  
        zaehler = 2
        for tag in range(2,monatlang+1,1): # Frage: was ist schneller? range(1,calfunctions.monatslaenge(monat))
            w+=1
            if(w%7==0): 
                print('\t'+str(zaehler),end='\n')
            elif (w%7==1):
                print(str(zaehler),end='')  
            else:
                print('\t'+str(zaehler),end='')   
            zaehler+=1 
        print(end='\n\n')
        
    # Gibt die Feiertage aus    
    feiertag = calfunctions.feiertage(jahr)
    for counter in range(0,len(feiertag),1):        
        print(feiertag[counter][2]+':\t'+str(feiertag[counter][1])+'. '+str(monatsname[feiertag[counter][0]-1]))
    
        
    
"""
from tkinter import *
fenster=Tk()

fenster.title("Hallo Welt")
fenster.geometry("600x1000")

nachricht[]=Message(fenster, text=ausgabe)
nachricht[].config(font=('times',8,'italic'))
nachricht[].pack()

ausgabe=[kalender(2015)]
print(ausgabe)
print(str(ausgabe))
#w=Label(fenster, text=str(ausgabe))
#w.pack()
fenster.mainloop()
"""

