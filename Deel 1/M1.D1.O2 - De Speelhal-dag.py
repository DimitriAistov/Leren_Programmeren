personen = 4

toegangsticket = 7.45
gameseat_5min = 0.37
tijd_prijs = 45/5

gameseat_prijs = gameseat_5min * tijd_prijs
gameseat_prijs_totaal = gameseat_prijs * personen
toegang_prijs = toegangsticket * personen

totaal_prijs = gameseat_prijs_totaal * toegang_prijs
totaal_prijs = round(totaal_prijs,2)
print("Uw totaalbedrag is: ", totaal_prijs)


