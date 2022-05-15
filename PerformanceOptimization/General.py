# coding: utf-8
"""
-------------------------------------------------
   File Name:      General
   Author :        Scar
   E-mail :        scarforhere@gmail.com
   Date:           2021-05-23 09:39 AM
-------------------------------------------------
Description : 

    Code erst optimieren, wenn tatsächlich Bedarf besteht:
        „Premature optimisation is the root of all evil.“

    Reihenfolge:
        „Make it run. Make it right. Make it fast.“

"""
import timeit
import time

'''01. Spezielle Bibliotheken für jeweiliges Problem verwenden'''
import numpy as np


def test01():
    x = np.linspace(0, 1000, 10000000)
    x *= 2


def test02():
    x = [i for i in range(0, 1000, 10000000)]
    for num, item in enumerate(x):
        x[num] = item * 2

# print(timeit.timeit(test01, number=100))
# print(timeit.timeit(test02, number=100))


'''02. Angemessene Datentypen verwenden: tuple oder dict statt list'''
dic = {}
for i in range(1000):
    dic[i] = True


def test03():
    if 3 in dic:  # Aufwand O(1)
        pass


def test04():
    if 3 in [i for i in range(1000)]:  # Aufwand O(n)
        pass

# print(timeit.timeit(test03, number=10000))
# print(timeit.timeit(test04, number=10000))


'''03. „Punkte“ (Objektorientierung) vermeiden:'''
# • jeder Punkt bedeutet Attribute/Member Lookup,
# • lokales Zwischenspeichern lohnt sich besonders in Schleifen
import math

wurzel = math.sqrt
wurzel(2)


'''04. Sog. list comprehension statt for -Schleife nutzen'''
def test05():
    r = [str(k) for k in range(10000000)]


def test06():
    r = []
    for k in range(10000000):
        r.append(str(k))


# print(timeit.timeit(test05, number=1))
# print(timeit.timeit(test06, number=1))


'''05. In (verschachtelten) Schleifen: Funktionalität „von innen nach außen“ verlagern'''
# – Initialisierungen von Variablen
# – Berechnungen --> Zwischenergebnisse Speichern/Cachen
# – Allgemein:
#     Anweisungen nur so oft wie nötig ausführen, aber so selten wie möglich


'''06. Iteratoren nutzen (z.B. range(4) statt [0, 1, 2, 3])'''
# – Hintergrund: Iteratoren erzeugen Funktion, um nächstes Element zu berechnen,
# – Oft effizienter als komplette Datenstruktur für Iteration im Vorfeld zu generieren
lst=[i for i in range(10000)]

def test07():
    x = [i for i in range(10000)]


def test08():
    x = [i for i in lst]


print(timeit.timeit(test07, number=100))
print(timeit.timeit(test08, number=100))


'''07. Lokale Variablen verwenden'''
# – der Zugriff ist hier schneller, als auf Variable außerhalb des aktuellen Namensraums
# – Funktionen vektorisieren für schnelle Array-Operationen ( numpy.vectorize )