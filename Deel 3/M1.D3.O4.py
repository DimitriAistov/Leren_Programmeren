Naam1 = "oorschot"

gastheer = input("Wie is de gastheer? ").lower()
gasten = True
drank = True
chips = True

if chips and drank and (gasten or gastheer) == True and gastheer != Naam1 and gastheer != "":
    print('Start the Party')
else:
    print('No Party')
