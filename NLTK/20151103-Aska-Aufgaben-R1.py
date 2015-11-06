"""
Aufgabe 0: Schreiben Sie einen Algorithmus, der alle Wörter in text6 findet, die mindestens
6 und maximal 10 Zeichen lang sind, und geben Sie sie nach Länge(!) sortiert aus.
"""
import nltk
from nltk.book import *

myTokens = set(text1)
myWordList = [word for word in myTokens if len(word) in range(6,10)]
#selfbuild sort by length
myResult = ['']
for myCount in range(6,10):
    myResult.append(sorted([word for word in myTokens if len(word) == myCount]))
myResult.pop(0)#entfernt das Nullwort

"""
Aufgabe 1:
a) Finden Sie in text7 alle Types, die einen Bindestrich in Kombination mit dem Wort „index“ beinhalten.
b) Welcher Befehl sucht sowohl Wörter mit Bindestrich als auch Wörter mit „index“ heraus?
"""
myText7 = set(text7);
myConnections = [word for word in  myText7 if '-' in word]
myConnections = [word for word in  myConnections if 'index' in word]

#b) tja...
# vielleicht über endswith?
myText7 = set(text7);
myConnections = [word for word in  myText7 if w.endswith('-index')]


"""
Aufgabe 2: Finden Sie in sent7 alle Types, die nicht aus Kleinbuchstaben bestehen.
""" 

#ist damit gemeint: nicht "nur"(!) aus Kleinbuchstaben
myResult = [word for word in sent7 if not(word.islower())]

#oder die überhaupt keineKleinbuchstaben verwenden?
# myResult2 = [word for word in sent7 if (not(word.islower()) and not(word.isupper()))]
# warum geht die Line obendrüber nicht?
myResult2 = [word for word in sent7 if (not(word.isalpha()))]

"""
Aufgabe 3: Formulieren Sie eine if-Struktur, welche bestimmt, ob der Wert der Variablen x positiv, negativ
oder gleich Null ist.
"""
def what_sig(x):
    if (x > 0):
        return 'positive'
    elif (x < 0):
        return 'negative'
    else:
        return 'zero'


	 	  
"""
Aufgabe 4: Definiert wurden drei Variablen mit den entsprechen Werten: x = 5, y = 50 und z = 1
Formulieren Sie eine if-Struktur, welche bestimmt, ob der Wert der Variablen x größer als die
Variable y und kleiner als die Variable z ist. Sollte dies nicht der Fall sein, lassen Sie diese durch ein print() ausgeben.
""" 
if not(x > y and y > z):
    print(x)

"""
Aufgabe 5: Formulieren Sie eine for-Schleife, um alle Wörter im text1, welche mit dem Anfangsbuchstaben „Z“, oder „z“ beginnen, zu finden.
"""
myWords = ['']
for myCount in range(len(text1)):
    help = text1[myCount]
    if (help[0] == 'z' or help[0] == 'Z'):
        myWords.append(help)
myWords.pop(0)

