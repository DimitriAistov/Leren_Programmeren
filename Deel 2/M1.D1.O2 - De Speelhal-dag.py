TOEGANGSTICKET = 7.45
GAMESEAT_5MIN = 0.37

hoeveelheid_mensen = int(input("Hoeveel mensen? "))
hoeveelheid_tijd = int(input("Hoeveel 5 minuut pakketen wilt u hebben? "))

tijd_hoeveelheid = hoeveelheid_tijd * GAMESEAT_5MIN
toegangkosten = TOEGANGSTICKET * hoeveelheid_mensen
tijdkosten = tijd_hoeveelheid * hoeveelheid_mensen



totaal_prijs = toegangkosten + tijdkosten
totaal_prijs = round(totaal_prijs,2)
print(f"Dit geweldige dagje-uit met {hoeveelheid_mensen} mensen in de Speelhal met {tijd_hoeveelheid} minuten VR kost je maar {totaal_prijs} euro")


