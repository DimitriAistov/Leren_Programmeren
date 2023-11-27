gastheer = True
gasten = True
drank = True
chips = True

if chips and drank and (gasten or gastheer) == True:
    print('Start the Party')
else:
    print('No Party')
