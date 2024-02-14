nr1 = int(input("Kies eerste getal: "))
nr2 = int(input("Kies tweede getal: "))

def meten(nr1,nr2):
    if nr1 == nr2:
        return(f"Beide getallen zijn even groot")
    elif nr1>nr2:
        return(f"Maximum: {nr1} en minimum: {nr2}")
    elif nr1<nr2:
        return(f"Maximum: {nr2} en minimum: {nr1}")

print(meten(nr1, nr2))