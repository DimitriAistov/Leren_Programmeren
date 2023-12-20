from studieadviestext import*

print (COMPETENTIE_STELLING_1)
opties1 = OPTIES
print(opties1)
opties1 = int(input(""))

print (COMPETENTIE_STELLING_2)
opties2 = OPTIES
print(opties2)
opties2 = int(input(""))

print (COMPETENTIE_STELLING_3)
opties3 = OPTIES
print(opties3)
opties3 = int(input(""))

uitkomst = round(opties1 + opties2 + opties3) /3

if uitkomst ==3:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
elif uitkomst <3:
    print(COMPETENTIE_ADVIES_ZORGELIJK)
else:
    print(COMPETENTIE_ADVIES_GERUSTSTELLEND)