rijbewijs = input("Heeft U een vrachtwagen rijbewijs? Ja/Nee ").lower()
hoed = input("Bent U in het bezit van een hoge hoed? Ja/Nee ").lower()
gewicht = int(input("Wat is uw lichaamsgewicht in hele kg? "))
ervaringDieren = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
ervaringJongleren = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? "))
ervaringAcrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))

GEWICHT_MIN = 90
GEWICHT_MAX = 120
ERVARING_DIEREN_MIN = 4
ERVARING_JONGLEREN_MIN = 5
ERVARING_ACROBATIEK_MIN = 5

if rijbewijs == "ja" and hoed == "ja" and (gewicht > GEWICHT_MIN and gewicht < GEWICHT_MAX) and (ervaringDieren > ERVARING_DIEREN_MIN or ervaringJongleren > ERVARING_JONGLEREN_MIN or ervaringAcrobatiek > ERVARING_ACROBATIEK_MIN):
    print("Je hebt de baan!")
else:
    print("Je hebt de baan niet.")

