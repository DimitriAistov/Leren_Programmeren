Naam1 = "oorschot"

gastheer = input("Wie is de gastheer? ").lower()
gasten = int(input("Hoeveel gasten zijn er? "))
drank = True
chips = True

if chips and drank and (gasten or gastheer) == True and gastheer != Naam1 and gastheer != "" and gasten >0 or gasten <20:
    print('Start the Party')
else:
    print('No Party')
