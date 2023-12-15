getalA = int(input("Kies eerste getal: "))
getalB = int(input("Kies tweede getal: "))
max = getalA
min = getalB


if getalA > getalB:
    max = getalA
    min = getalB
    print(f"'A' is het grootste getal {max}")

elif getalA < getalB:
    min = getalA
    max = getalB
    print(f"'A' is het kleinste getal {min}")

else:
    print(f"'A' en 'B' zijn even groot")

print(f"Het minimum is {min}")
print(f"Het maximum is {max}")