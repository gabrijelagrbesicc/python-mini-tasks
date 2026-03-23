"""
Napisati Python funkciju koja filtrira vrijednosti rjecnika na osnovu visine i kao rezultat
daje novi rjecnik. Argumenti funkcije trebaju biti rjecnik, i visina po kojoj se filtrira.
(primjer: filtrira sve osobe koje su vece od odredene visine)
Rjecnik:
{'Pero Peric': 175, 'Marko Markic': 180, 'Jure Juric': 165, 'Marija Maric': 190}

osobe = {
    "Pero Peric":175,
    'Marko Markic':180,
    "Jure Juric":165,
    "Marija Maric":190
}

def filtriraj(rjecnik,granica):
    novi={}

    for ime,visina in rjecnik.items():
        if visina > granica:
            novi[ime] = visina
    
    return novi


rezultat = filtriraj(osobe, 175)
print("Te osobe su:",rezultat)"""

"""
Napiši funkciju koja vraća osobe niže od zadane visine.


osobe = {
    "Pero Peric":175,
    'Marko Markic':180,
    "Jure Juric":165,
    "Marija Maric":190
}

def filtriraj(rjecnik,granica):
    novi={}

    for ime,visina in rjecnik.items():
        if visina < granica:
            novi[ime] = visina

    return novi

rez = filtriraj(osobe, 180)
print("Te osobe su:",rez)"""

"""
Napiši funkciju koja vraća ukupnu visinu svih osoba u rječniku.

osobe = {
    "Pero Peric":175,
    'Marko Markic':180,
    "Jure Juric":165,
    "Marija Maric":190
}

def ukupnaVisina(osobe):
    suma=0
    for visina in osobe.values():
        suma += visina
    return suma

rez = ukupnaVisina(osobe)
print("Suma visina: ",rez)"""

"""
Napiši funkciju koja računa prosječnu visinu.


osobe = {
    "Pero Peric":175,
    'Marko Markic':180,
    "Jure Juric":165,
    "Marija Maric":190
}

def prosjek(osobe):
    suma=0
    prosjek=0.0
    for visina in osobe.values():
        suma+=visina
    prosjek = suma / len(osobe)
    return prosjek

rez = prosjek(osobe)
print("Prosjek visina je: ",rez)"""

"""
Napiši funkciju koja vraća ime i visinu najviše osobe.

osobe = {
    "Pero Peric":175,
    'Marko Markic':180,
    "Jure Juric":165,
    "Marija Maric":190
}

def najvisa(osobe):
    imeM=""
    visinaMax=0

    for ime,visina in osobe.items():
        if visina>visinaMax:
            visinaMax = visina
            imeM = ime
    return imeM,visinaMax

ime,visina = najvisa(osobe)
print("Najvisa osoba je ",ime,",a visoka je ",visina,"cm")"""

"""
Napiši funkciju koja vraća koliko osoba je veće od određene visine.


osobe = {
    "Pero Peric":175,
    'Marko Markic':180,
    "Jure Juric":165,
    "Marija Maric":190
}


def kolikoJe(osobe,granica):
    brojac=0
    for visina in osobe.values():
        if visina > granica:
            brojac += 1
    return brojac

rez = kolikoJe(osobe,180)
print("Broj osoba koje su vece od 180:",rez)"""

"""
Napiši funkciju koja vraća novi rječnik sa osobama čije ime: počinje na određeno slovo

osobe = {
    "Pero Peric":175,
    "Marko Markic":180,
    "Jure Juric":165,
    "Marija Maric":190
}

def nova(osobe, slovo):
    novi = {}

    for ime, visina in osobe.items():
        if ime.startswith(slovo):
            novi[ime] = visina

    return novi

rez = nova(osobe, "P")
print(rez)"""

"""
Napiši funkciju koja: povećava sve visine za +5 cm

osobe = {
    "Pero Peric":175,
    "Marko Markic":180,
    "Jure Juric":165,
    "Marija Maric":190
}

def povecaj(osobe):
    novi = {}
    for ime,visina in osobe.items():
        novi[ime] = visina + 5
    return novi

rez = povecaj(osobe)
print(rez)"""

"""
Napiši funkciju koja zamjenjuje: ime -> visina u: visina -> ime
"""

osobe = {
    "Pero Peric":175,
    "Marko Markic":180,
    "Jure Juric":165,
    "Marija Maric":190
}

def zamijeni(osobe):
    novi = {}
    for ime,visina in osobe.items():
        novi[visina] = ime
    return novi

rez = zamijeni(osobe)
print(rez)