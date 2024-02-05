#Dimitri Aistov Pizza Calculator
try:
    small = float(input("Hoeveel kleine pizzas wilt u? "))
    medium = float(input("Hoeveel medium pizzas wilt u? "))
    large = float(input("Hoeveel grote pizzas wilt u? "))

    if not all(A.is_integer() for A in [small, medium, large]):
        raise ValueError("Het aantal pizza's moet een geheel getal zijn.")

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
    print(f"{int(small)} kleine pizzas: €{smallkosten:.2f}")
    print(f"{int(medium)} medium pizzas: €{mediumkosten:.2f}")
    print(f"{int(large)} grote pizzas: €{largekosten:.2f}")
    print(f"Uw totaalbedrag is €{totaalprijs:.2f}")

except ValueError as ve1:
    print(f"Foutieve invoer: {ve1}")
except Exception as ve2:
    print(f"Er is een fout opgetreden: {ve2}")



