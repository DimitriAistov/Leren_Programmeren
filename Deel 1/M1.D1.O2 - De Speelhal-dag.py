PERSONEN = 4

TOEGANGSTICKET = 7.45
GAMESEAT_5MIN = 0.37
TIJD_PRIJS = 45/5

gameseat_prijs = GAMESEAT_5MIN * TIJD_PRIJS
gameseat_prijs_totaal = gameseat_prijs * PERSONEN
toegang_prijs = TOEGANGSTICKET * PERSONEN

totaal_prijs = gameseat_prijs_totaal + toegang_prijs
totaal_prijs = round(totaal_prijs,2)
print(f"Dit geweldige dagje-uit met 4 mensen in de Speelhal met 45 minuten VR kost je maar {totaal_prijs} euro")


