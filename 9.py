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
"""

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

print(prosjek_rjecnik)