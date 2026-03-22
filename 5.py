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
generira listu od 100 brojeva (1–10) pronalazi i ispisuje broj koji se najviše puta pojavljuje"""

import random

lista = []

for i in range(100):
    lista.append(random.randint(0,10))

print("Lista: ", lista)

maxBroj=0
maxPon=0

for broj in range(11):
    brojac = lista.count(broj)

    if(brojac > maxPon):
        maxPon = brojac
        maxBroj = broj

print("Najcesci broj je ", maxBroj)
print("Ponovio je se ", maxPon," puta")