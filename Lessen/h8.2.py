import random
import timeit

getallist = list(getal*10 for getal in range(100_000))
getaldict = {getal*10 : 0 for getal in range(100_000)}

zoekgetal = random.randrange(1_000_000)

starttime = timeit.default_timer()
if zoekgetal in getallist :
    print('gevonden in lijst')
else :
    print('niet gevonden in lijst')
print("zoektijd in de lijst :", timeit.default_timer() - starttime)

starttime = timeit.default_timer()
if zoekgetal in getaldict :
    print('gevonden in woordenboek')
else :
    print('niet gevonden in woordenboek')
print("zoektijd in het woordenboek :", timeit.default_timer() - starttime)