SLB = "oorschot"
NAAM = "dimitri"

gastheer = input("Wie is de gastheer? ").lower()
gasten = True
drank = True
chips = True

noParty = "No Party"
party = "Start the Party"

if chips and drank and (gastheer != "" or gastheer == NAAM or gastheer != SLB):
    print(party)
elif gastheer != "" and chips:
    print(party)
else:
    print(noParty)
