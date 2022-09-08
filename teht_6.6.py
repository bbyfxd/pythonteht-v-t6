import math


def PizzanArvo(halkaisijaCm, hinta):
    sade = float(halkaisijaCm / 2)
    PintaAlaM = (math.pi * sade * sade) / 10000
    arvo = hinta / PintaAlaM
    return arvo

pizzat = []

lmk = int(input("Monta pizzaa? "))
for x in range(lmk):
    print(f"Anna pizza {x+1}. pizzan tiedot: ")
    hinta = float(input("Syötä pizzan hinta: "))
    halkisija = float(input("Syötä pizzan halkisija: "))
    pizzat.append(PizzanArvo(halkisija, hinta))

arvokkaimmanId = 0
for x in range(2):
    if pizzat[arvokkaimmanId] > pizzat[x]:
        arvokkaimmanId = x

print(f"Arokkain (paras hinta-kokosuhde) pizza on {arvokkaimmanId+1}. pizza.")