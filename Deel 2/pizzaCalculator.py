#Dimitri Aistov Pizza Calculator
small = int(input("Hoeveel kleine pizzas wilt u? "))
medium = int(input("Hoeveel medium pizzas wilt u? "))
large = int(input("Hoeveel grote pizzas wilt u? "))

#prijzen
SMALL_PRIJS = 6.50
MEDIUM_PRIJS = 8
LARGE_PRIJS = 11

#kosten
smallkosten = small * SMALL_PRIJS
mediumkosten = medium * MEDIUM_PRIJS
largekosten = large * LARGE_PRIJS
totaalprijs = smallkosten + mediumkosten + largekosten

#output
print(f"Uw bestelling: ")
print(f"{small} kleine pizzas: €{smallkosten}")
print(f"{medium} medium pizzas: €{mediumkosten}")
print(f"{large} large pizzas: €{largekosten}")
print(f"Uw totaalbedrag is €{totaalprijs}")
