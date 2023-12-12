from studieadviestext import*

print (COMPETENTIE_STELLING_1)
opties1 = OPTIES
print(opties1)
opties1 = int(input(""))

print (COMPETENTIE_STELLING_2)
opties2 = OPTIES
print(opties2)
opties2 = int(input(""))

uitkomst = opties1 + opties2

if uitkomst >=6:
    print (COMPETENTIE_ADVIES_GERUSTSTELLEND)
elif uitkomst ==5:
    print(COMPETENTIE_ADVIES_TWIJFELACHTIG)
elif uitkomst <=4:
    print(COMPETENTIE_ADVIES_ZORGELIJK)