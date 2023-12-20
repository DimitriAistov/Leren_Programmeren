gastheer = True
gasten = False
drank = False
chips = True

noParty = "No Party"
party = "Start the Party"

if chips and drank and (gasten or gastheer) == True:
    print(party)
elif gastheer and chips == True:
    print(party)
else:
    print(noParty)
