#Dimitri Aistov Pizza Calculator
small = int(input("Hoeveel kleine pizzas wilt u? "))
medium = int(input("Hoeveel medium pizzas wilt u? "))
large = int(input("Hoeveel grote pizzas wilt u? "))

#prijzen
smallprijs = 6
mediumprijs = 8
largeprijs = 11

#kosten
smallkosten = small * smallprijs
mediumkosten = medium * mediumprijs
largekosten = large * largeprijs
totaalprijs = smallkosten + mediumkosten + largekosten

#output
print(f"Uw bestelling: ")
print(f"{small} kleine pizzas: €{smallkosten}")
print(f"{medium} medium pizzas: €{mediumkosten}")
print(f"{large} large pizzas: €{largekosten}")
print(f"Uw totaalbedrag is €{totaalprijs}")
