bedrag = float(input("Hoeveel is het bedrag? "))

def prijs():
    return round(bedrag * 100 / 5) * 5 / 100
    
totaalprijs_afgerond = "{:.2f}".format(prijs())

print(totaalprijs_afgerond)

