"""Napisi program koji ispisuje cjelobrojne elemente koji se pojavljuju 3 ili vise puta unutar
liste. Generiraj listu od 100 elemenata u rasponu vrijednosti od 0 do 30.

import random

lista = []
for i in range(100):
    lista.append(random.randint(0,30))

print("Lista: ",lista)

for broj in range(31):
    if lista.count(broj) >= 3:
        print(broj, " se pojavljuje ", lista.count(broj)," puta")"""

""""
Napiši program koji: generira listu od 50 brojeva (0–20) ispisuje sve brojeve koji se pojavljuju barem 2 puta

import random

lista = []

for i in range(50):
    lista.append(random.randint(0,20))
print("Lista: ",lista)

for broj in range(21):
    if lista.count(broj) >= 2:
        print(broj, " se ponavlja ",lista.count(broj)," puta")
"""

"""
Napiši program koji:
generira listu od 100 brojeva (1–10) pronalazi i ispisuje broj koji se najviše puta pojavljuje

import random

lista = []

for i in range(100):
    lista.append(random.randint(1,10))

print("Lista: ", lista)

maxBroj=0
maxPon=0

for broj in range(1,11):
    brojac = lista.count(broj)

    if(brojac > maxPon):
        maxPon = brojac
        maxBroj = broj

print("Najcesci broj je ", maxBroj)
print("Ponovio je se ", maxPon," puta")
"""
"""
Napiši program koji:
generira listu od 30 brojeva (1–100) ispisuje:
koliko ima parnih, akoliko ima neparnih
"""
""""
import random

lista = []

for i in range(30):
    lista.append(random.randint(1,100))

print("Lista: ",lista)

brojacP = 0
brojacN = 0
for broj in lista:
    if(broj % 2 == 0):
        brojacP = brojacP + 1
    else:
        brojacN = brojacN + 1

print("Broj parnih je ",brojacP,",a neparnih je ", brojacN)
"""
"""
Napiši program koji:
generira listu od 40 brojeva (0–20) i računa i ispisuje sumu svih brojeva većih od 10
"""

import random

lista = []

for i in range(40):
    lista.append(random.randint(0,20))
print("Lista: ", lista)

zbroj=0

for broj in lista:
    if broj > 10:
        zbroj += broj

print("Suma je ", zbroj)
