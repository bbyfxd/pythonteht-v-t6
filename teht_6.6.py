import math


def PizzanArvo(halkaisijaCm, hinta):
    sade = float(halkaisijaCm / 2)
    PintaAlaM = (math.pi * sade * sade) / 10000
    arvo = hinta / PintaAlaM
    return arvo

pizzat = []

for x in range(2):
    print(f"Anna pizza {x} tiedot: ")
    hinta = float(input("Syötä pizzan hinta: "))
    halkisija = float(input("Syötä pizzan halkisija: "))
    pizzat.append(PizzanArvo(halkisija, hinta))

arvokkaimmanId = 0
for x in range(2):
    if pizzat[arvokkaimmanId] < pizzat[x]:
        arvokkaimmanId = x

print(f"Arokkain pizza on indeksin {arvokkaimmanId} pizza.")