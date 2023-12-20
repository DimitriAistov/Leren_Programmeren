SLB = "oorschot"
NAAM = "dimitri"

gastheer = input("Wie is de gastheer? ").lower()
gasten = int(input("Hoeveel gasten zijn er? "))
drank = False
chips = True

party = "Start the Party"
noParty = "No Party"

if chips and drank and gastheer != SLB and gastheer != "" or gastheer == NAAM and gasten >=4 or gasten <=20:
    print(party)
elif gastheer != "" and chips:
    print(party)
elif gastheer == SLB:
    print(noParty)
else:
    print(noParty)
