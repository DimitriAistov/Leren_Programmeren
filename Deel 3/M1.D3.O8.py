GEWICHT_MIN = 90
GEWICHT_MAX = 120
ERVARING_DIEREN_MIN = 4
ERVARING_JONGLEREN_MIN = 5
ERVARING_ACROBATIEK_MIN = 5

rijbewijs = input("Heeft U een vrachtwagen rijbewijs? Ja/Nee ").lower()
hoed = input("Bent U in het bezit van een hoge hoed? Ja/Nee ").lower()
geslacht = input("Wat is uw geslacht? Man/Vrouw/Anders ").lower()

if geslacht == "man":
    snor = input("Heeft u een snor? Ja/Nee ").lower()
    geschiktheid_geslacht = snor == "ja"
elif geslacht == "vrouw":
    haar = input("Heeft u rood krulhaar? Ja/Nee ").lower()
    geschiktheid_geslacht = haar == "ja"
else:
    glimlach = input("Heeft u een brede glimlach? Ja/Nee ").lower()
    geschiktheid_geslacht = glimlach == "ja"

gewicht = int(input("Wat is uw lichaamsgewicht in hele kg? "))
ervaringDieren = int(input("Hoeveel jaar praktijkervaring heeft u met dieren-dressuur? "))
ervaringJongleren = int(input("Hoeveel jaar praktijkervaring heeft u met jongleren? "))
ervaringAcrobatiek = int(input("Hoeveel jaar praktijkervaring heeft u met acrobatiek? "))

niet_aangenomen = []

if rijbewijs != "ja":
    niet_aangenomen.append("Moet in het bezit zijn van een vrachtwagen rijbewijs")
if hoed != "ja":
    niet_aangenomen.append("Moet in het bezit zijn van een hoge hoed")

if not (GEWICHT_MIN < gewicht < GEWICHT_MAX):
    niet_aangenomen.append(f"Gewicht moet tussen {GEWICHT_MIN} en {GEWICHT_MAX} kg liggen")
if not (ervaringDieren > ERVARING_DIEREN_MIN or ervaringJongleren > ERVARING_JONGLEREN_MIN or ervaringAcrobatiek > ERVARING_ACROBATIEK_MIN):
    niet_aangenomen.append("Je hebt niet genoeg ervaring hebben met dieren-dressuur, jongleren of acrobatiek")
if not geschiktheid_geslacht:
    niet_aangenomen.append("Voldoet niet aan geslachtscriteria")
if not niet_aangenomen:
    print("Je hebt de baan!")
else:
    print("Je hebt de baan niet omdat:")
    for reden in niet_aangenomen:
        print(reden)
