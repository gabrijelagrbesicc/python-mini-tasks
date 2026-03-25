"""
Za dani riječnik čiji su ključevi imena studenata, a vrijednosti ocjene. Vrijednosti trebaju
biti u obliku ntorke. Potrebno je vratiti rječnik čiji će ključevi biti prosječna ocjena
(zaokružena - koristiti round() funkciju),a vrijednosti sortirana lista studenata koji su
dobili tu prosječnu ocjenu.
Npr. u rječniku {'ivan': (3,2,4), 'marko': (5,5,4), 'ana': (2,3,4)}, 'ivan' ima ocjene 3, 2, 4 i
prosječna ocjena je 3.0, 'marko' ima ocjene 5, 4 i prosječna ocjena je 4.0, 'ana' ima
ocjene 2, 3, 4 i prosječna ocjena je 3.0.
 Izlazni rječnik će biti {3: ['ana', 'ivan'], 4: ['marko']} jer 'ivan' i 'ana' imaju prosjek 3.0, a
'marko' prosjek 4 


ocjene_studenata = {
    'ivan': (3, 2, 4),
    'marko': (5, 5, 4),
    'ana': (2, 3, 4)
}

prosjek_rjecnik = {}

for student, ocjene in ocjene_studenata.items():
    prosjek = round(sum(ocjene) / len(ocjene))  
    if prosjek not in prosjek_rjecnik:
        prosjek_rjecnik[prosjek] = []
    prosjek_rjecnik[prosjek].append(student)

for studenti in prosjek_rjecnik.values():
    studenti.sort()

print(prosjek_rjecnik)"""

"""
Napravi novi rječnik gdje će ključevi biti zadnje slovo imena, a vrijednosti lista zaposlenika koji imaju to slovo na kraju imena.
Lista zaposlenika treba biti sortirana po abecedi.

zaposlenici = {
    'Ana': 3000,
    'Ivan': 3500,
    'Marko': 4000,
    'Lana': 3200,
    'Maja': 3100
}

novi = {}

for ime in zaposlenici:
    zadnjeSlovo = ime[-1]
    if zadnjeSlovo not in novi:
        novi[zadnjeSlovo] = []
    novi[zadnjeSlovo].append(ime)

for slovo in novi:
    novi[slovo].sort()

print(novi)"""

"""
Napravi rječnik gdje su ključevi 'parni' ili 'neparni' ovisno o zaokruženom prosjeku ocjena, a vrijednosti su liste učenika koji imaju prosjek u toj kategoriji.
Liste treba sortirati po abecedi.


ocjeneS = {
    'Ivan': [3,4,5],
    'Ana':[5,5,4],
    'Marko':[2,3,3],
    'Lana':[4,4,4]
}

novi = {}

for ime,ocjene in ocjeneS.items():
    prosjek = round(sum(ocjene) / len(ocjene))
    if prosjek % 2 == 0:
        if "parni" not in novi:
            novi["parni"] = []
        novi['parni'].append(ime)
    else:
        if "neparni" not in novi:
            novi["neparni"] = []
        novi["neparni"].append(ime)


for o in novi:
    novi[o].sort()

print(novi)"""

"""
Podijeli proizvode u tri kategorije:
'jeftino' (< 3 kn)
'srednje' (3–5 kn)
'skupo' (> 5 kn)
Napravi rječnik gdje su ključevi kategorije, a vrijednosti lista proizvoda u toj kategoriji, sortirana po abecedi.


proizvodi = {
    'mlijeko': 2.5,
    'kruh': 1.2,
    'sir': 3.0,
    'jaja': 4.5,
    'maslac': 5.0,
    'jogurt' : 6.0
}

novi = {}

for proizvod,cijena in proizvodi.items():
    if cijena < 3:
        if "jeftino" not in novi:
            novi["jeftino"] = []
        novi['jeftino'].append(proizvod)
    elif 3<=cijena<=5:
        if "srednje" not in novi:
            novi["srednje"] = []
        novi['srednje'].append(proizvod)
    else:
        if "skupo" not in novi:
            novi["skupo"] = []
        novi['skupo'].append(proizvod)

for kljuc in novi:
    novi[kljuc].sort()

print(novi)"""

"""
Napravi rječnik gdje su ključevi prvo slovo imena, a vrijednosti lista imena koja počinju tim slovom, sortirana po abecedi.

studenti = {
    'Ana': 4,
    'Ivan': 5,
    'Marko': 3,
    'Maja': 5,
    'Lana': 4
}

novi = {}

for ime,ocjena in studenti.items():
    prvoSlovo = ime[:1]
    if prvoSlovo not in novi:
        novi[prvoSlovo] = []
    novi[prvoSlovo].append(ime)

for kljuc in novi:
    novi[kljuc].sort()

print(novi)"""

"""
Napravi rječnik gdje su ključevi duljina riječi, a vrijednosti lista riječi te duljine, sortirana po abecedi.

rijeci = {
    'sunce': 'sun',
    'mjesec': 'moon',
    'zvijezda': 'star',
    'planina': 'mountain',
    'klanins': 'dafjao'
}

novi = {}

for rijec in rijeci:
    kljuc = len(rijec)
    if kljuc not in novi:
        novi[kljuc] = []
    novi[kljuc].append(rijec)

for k in novi:
    novi[k].sort()

print(novi)"""

"""
Napravi rječnik gdje su ključevi ocjene, a vrijednosti liste učenika koji imaju tu ocjenu, sortirane po abecedi.
"""

učenici = {
    'Ivan': 4,
    'Ana': 5,
    'Marko': 3,
    'Maja': 5,
    'Lana': 4
}

novi = {}

for ime, ocjena in učenici.items():
    if ocjena not in novi:
        novi[ocjena] = []
    novi[ocjena].append(ime)

for k in novi:
    novi[k].sort()

print(novi)