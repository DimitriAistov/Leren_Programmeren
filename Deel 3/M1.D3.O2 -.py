geel = input("Is de kaas geel? ").lower()
if geel == "ja":
    gaten = input("Zitten er gaten in? ").lower()
    if gaten == "ja":
        duur = input("Is de kaas belachelijk duur? ").lower()
        if duur == "ja":
            print("Emmenthaler")
        else:
            print("Leerdammer")
    else:
        hard = input("Is de kaas hard als steen? ").lower()
        if hard == "ja":
            zoutig = input("Is de kaas zout")
            if zoutig =="ja":
                print("Old Amsterdammer")
            else:
                print("Parmigiano Reggiano")
        else:
            print("Goudse kaas")
else:
    schimmel = input("Heeft de kaas blauwe schimmel? ").lower()
    if schimmel == "ja":
        korst1 = input("Heeft de kaas korst? ").lower()
        if korst1 =='ja':
            print("Bleu de Rochebaron")
        else:
            print("Foume d'ambert")
    else:
        korst2 = input("Heeft de kaas korst? ").lower()
        if korst2 == "ja":
            print("Camembert")
        else:
            print("Mozzarella")