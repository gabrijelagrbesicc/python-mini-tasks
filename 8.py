"""
Kreirati listu prirodnih brojeva od 50 elemenata (koristiti random funkciju). Za danu
listu prirodnih brojeva stvori rječnik u kojemu će se nalaziti frekvencija pojavljivanja
određene brojčane znamenke u svim brojevima iz liste
Npr. za [423, 54, 45] broj 4 se pojavljuje 3 puta, 2 - 1 put, 3 -1 put, itd
Napomena: ključevi rječnika neka budu brojevi, a ne stringovi. 


import random

lista = []

for i in range(50):
    lista.append(random.randint(1,500))
print("Lista:",lista)

rjecnik={}

for broj in lista:
    for znamenka in str(broj):
        znamenka = int(znamenka)

        if znamenka in rjecnik:
            rjecnik[znamenka] += 1
        else:
            rjecnik[znamenka] = 1

print("Frekvencija znamneki:", rjecnik)"""

"""
Nađi koja se znamenka najviše pojavljuje

import random

lista = []

for i in range(10):
    lista.append(random.randint(1, 30))
print("Lista:", lista)

najcesci=None
maxBr=0

for broj in lista:
    koliko = lista.count(broj)

    if koliko > maxBr:
        maxBr = koliko
        najcesci = broj

print("Najčešća znamenka je:", najcesci)
print("Pojavljuje se:", maxBr, "puta")"""

"""
Generiraj listu od 30 brojeva (1–10) i napravi rječnik:
👉 broj → koliko puta se pojavljuje


import random

lista = []

for i in range(20):
    lista.append(random.randint(1, 10))
print("Lista:", lista)

rjecnik={
    "parni" : [],
    "neparni": []
}

for broj in lista:
    if broj % 2 == 0:
        rjecnik["parni"].append(broj)
    else:
        rjecnik["neparni"].append(broj)

print("Rjecnik: ",rjecnik)"""

"""
Generiraj listu i napravi rječnik:

{
    "manji_od_50": ?, 
    "veci_od_50": ?
}
"""

import random

lista = []

for i in range(20):
    lista.append(random.randint(1, 100))
print("Lista:", lista)

rjecnik = {
    "manjiOd50": [],
    "veciOd50": []
}

for broj in lista:
    if broj > 50:
        rjecnik["veciOd50"].append(broj) #dodajemo u listu pod kljucem veciOd50"
    else:
        rjecnik["manjiOd50"].append(broj)

print("Rjecnik:",rjecnik)