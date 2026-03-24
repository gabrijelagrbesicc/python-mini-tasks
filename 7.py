"""
Napisi program i funkciju loto642 koja simulira loto 6/42.
a. Funkcija izvlaci 6 brojeva te jedan dopunski broj preko generatora slučajnih
brojeva. Funkcija vraća listu loto brojeva.
b. Brojeve igrača možete unijeti prilikom inicijalizacije liste (ručno). 
"""

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
    print("Pogoden je dopunski broj")