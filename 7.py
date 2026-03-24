"""
Napisi program i funkciju loto642 koja simulira loto 6/42.
a. Funkcija izvlaci 6 brojeva te jedan dopunski broj preko generatora slučajnih
brojeva. Funkcija vraća listu loto brojeva.
b. Brojeve igrača možete unijeti prilikom inicijalizacije liste (ručno). 

import random

def loto642():
    brojevi=[]

    while len(brojevi)<7:
        broj = random.randint(1,42)
        if broj not in brojevi:
            brojevi.append(broj)

    return brojevi

igrac = [4,10,27,22,2,17]

izvuceni = loto642()

glavni = izvuceni[:6]
dopunski = izvuceni[6]

print("Izvuceni brojevi: ",glavni)
print("Dopunski broj: ",dopunski)

pogodak=0

for broj in igrac:
    if broj in glavni:
        pogodak += 1

print("Igrac ima",pogodak," pogotka")

if dopunski in igrac:
    print("Pogoden je dopunski broj")"""

"""
5 brojeva od 1–35 bez ponavljanja ispis pogodaka  

import random

def loto():
    brojevi=[]

    while len(brojevi)<5:
        broj = random.randint(1,35)
        if broj not in brojevi:
            brojevi.append(broj)
    return brojevi

rand = loto()

print("Izvuceni brojevi su:",rand)"""

"""
generiraj loto sortiraj brojeve uzlazno
"""

import random

def loto():
    brojevi=[]
    
    while(len(brojevi))<5:
        broj = random.randint(1,50)
        if broj not in brojevi:
            brojevi.append(broj)
    return brojevi

rez = loto()
print("Izvuceni brojevi:",rez)
igrac = [1,13,19,10,2]

def brojPogodaka():
    pogodak=0
    for broj in igrac:
        if broj in rez:
            pogodak += 1
    return pogodak

pog = brojPogodaka()
print("Igracevi brojevi:",igrac)

def sortiranje(rez):
    rez.sort()
    return rez

print("Igrac je pogodio ",pog," brojeva")
print("Sortirani loto brojevi", sortiranje(rez))


