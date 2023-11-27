CROISSANT_PRIJS = 0.39
STOKBROOD_PRIJS = 2.78
KORTINGSBON = 0.50

croissant_hoeveelheid = int(input("Hoeveel croissantjes wilt u? "))
stokbrood_hoeveelheid = int(input("Hoeveel stokbroden wilt u? "))
korting_hoeveelheid = int(input("Hoeveel kortingsbonnen heeft u? "))

croissant_totaal = CROISSANT_PRIJS * croissant_hoeveelheid
stokbrood_totaal = STOKBROOD_PRIJS * stokbrood_hoeveelheid
korting_totaal = KORTINGSBON * korting_hoeveelheid

totaal_prijs = croissant_totaal + stokbrood_totaal - korting_totaal
totaal_prijs = round(totaal_prijs,2)
print(f"De feestlunch kost je bij de bakker {totaal_prijs} euro voor de {croissant_hoeveelheid} croissantjes en de {stokbrood_hoeveelheid} stokbroden als de {korting_hoeveelheid} kortingsbonnen nog geldig zijn!")