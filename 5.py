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
"""
"""
Napiši program koji: generira listu od 20 brojeva (1–50) ispisuje: najmanji broj najveći broj


import random

lista = []

for i in range(20):
    lista.append(random.randint(1,50))

print("Lista: ",lista)

min=lista[0]
max=lista[0]

for broj in lista:
    if broj > max:
        max = broj
    if broj < min:
        min = broj

print("Najveci broj je ",max,",a najmanji ",min)"""

"""
Napiši program koji: generira listu od 50 brojeva (0–10) za svaki broj ispisuje koliko se puta pojavljuje

import random

lista = []

for i in range(50):
    lista.append(random.randint(0,10))
print("Lista: ",lista)


for broj in range(1,11):
    brojac = lista.count(broj)

    print(broj, "se ponavlja ", brojac, " puta.")"""

"""
Napiši program koji: generira listu od 30 brojeva (1–100) pravi novu listu koja sadrži samo brojeve: veće od 50 ispisuje novu listu

import random

lista = []
nova = []

for i in range(30):
    lista.append(random.randint(1,100))
print("Lista: ", lista)

for broj in lista:
    if broj>50:
        nova.append(broj)

print("Nova lista: ",nova)"""

"""
Napiši program koji: generira listu od 10 brojeva (1–20) ispisuje: originalnu listu listu obrnutim redoslijedom


import random

lista = []

for i in range(10):
    lista.append(random.randint(1,20))
print("Lista: ",lista)

obrnuta = lista[::-1]
print("Obrnuta lista: ",obrnuta)
"""

"""
Napiši program koji: generira slučajan broj od 1 do 20 korisnik pogađa broj program govori: "veći je" "manji je" dok ne pogodi

import random

broj = random.randint(1,20)

pogodak = int(input("Pogodi broj:"))

while pogodak != broj:
    if pogodak>broj:
        print("Broj je manji.Pokusaj opet")
    else:
        print("Broj je veci.Pokusaj opet")

    pogodak = int(input("Pogodi broj:"))

print("Bravo pogodili ste broj")"""

"""
Napiši program koji: generira listu od 50 brojeva (0–15) ispisuje brojeve koji se pojavljuju tačno 1 put

import random

lista = []
nova = []

for i in range(50):
    lista.append(random.randint(0,15))
print("Lista: ",lista)

for broj in range(16):
    brojac = lista.count(broj)

    if brojac==1:
        nova.append(broj)

print("Novi brojevi:",nova)"""

"""
Napiši program koji: generira listu od 100 brojeva (0–20) ispisuje: sve brojeve koji se pojavljuju ≥3 puta koliko takvih brojeva ima
"""

import random

lista = []
nova = []
koliko=0
for i in range(100):
    lista.append(random.randint(0,20))
print("Lista: ",lista)

for broj in range(21):
    brojac = lista.count(broj)

    if brojac >= 3:
        nova.append(broj)
        koliko += 1

print("Brojevi koji se ponavljanju 3 ili vise puta su:",nova)
print("Takvih brojeva je: ",koliko)

