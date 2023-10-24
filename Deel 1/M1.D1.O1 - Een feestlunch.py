croissant_prijs = 0.39
stokbrood_prijs = 2.78
kortingsbon = 0.50

croissant_totaal = croissant_prijs * 17
stokbrood_totaal = stokbrood_prijs * 2
korting_totaal = kortingsbon * 3

totaal_prijs = croissant_totaal + stokbrood_totaal - korting_totaal
print(f"De feestlunch kost je bij de bakker {totaal_prijs} euro voor de 17 croissantjes en de 2 stokbroden als de 3 kortingsbonnen nog geldig zijn!")