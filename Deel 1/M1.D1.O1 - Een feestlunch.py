CROISSANT_PRIJS = 0.39
STOKBROOD_PRIJS = 2.78
KORTINGSBON = 0.50

croissant_totaal = CROISSANT_PRIJS * 17
stokbrood_totaal = STOKBROOD_PRIJS * 2
korting_totaal = KORTINGSBON * 3

totaal_prijs = croissant_totaal + stokbrood_totaal - korting_totaal
print(f"De feestlunch kost je bij de bakker {totaal_prijs} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")