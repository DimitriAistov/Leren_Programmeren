toegangsticket = 7.45
gameseat_5min = 0.37

hoeveelheid_mensen = int(input("Hoeveel mensen? "))
hoeveelheid_tijd = int(input("Hoeveel 5 minuut pakketen wilt u hebben? "))

tijd_hoeveelheid = hoeveelheid_tijd * 5
toegangkosten = toegangsticket * hoeveelheid_mensen
tijdkosten = hoeveelheid_tijd * hoeveelheid_mensen

totaal_prijs = toegangkosten * tijdkosten
totaal_prijs = round(totaal_prijs,2)
print(f"Dit geweldige dagje-uit met {hoeveelheid_mensen} mensen in de Speelhal met {tijd_hoeveelheid} minuten VR kost je maar {totaal_prijs} euro")


