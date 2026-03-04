fruit = {'appel': 'rood', 'banaan': 'geel'}
print(fruit['banaan'])

boodschappen = {'Appels': 6, 'Brood': 2}
print (boodschappen['Brood'])
print(boodschappen.get('Appels', 'Appels staat niet in het woordenboek'))
print(boodschappen.get('Banenen', 'Banenen staat niet in het woordenboek'))


boodschappenlijst_marie = {'Brood': 1, 'Appels': 6}
boodschappenlijst_raj = {'Brood': 1, 'Appels': 6}
boodschappenlijst_jan = {'Appels': 6, 'Brood': 1}
boodschappenlijst_karel = {'Appels': 6, 'Brood': 25}

if boodschappenlijst_raj == boodschappenlijst_marie:
    print ("De boodschappenlijstjes zijn gelijk")

else:
    print ("Lijsten zijn niet gelijk")

if boodschappenlijst_raj == boodschappenlijst_marie == boodschappenlijst_jan:
    print ("De boodschappenlijstjes zijn gelijk")

else:
    print ("Lijsten zijn niet gelijk")

if boodschappenlijst_raj == boodschappenlijst_marie == boodschappenlijst_jan == boodschappenlijst_karel:
    print ("De boodschappenlijstjes zijn gelijk")

else:
    print ("Lijsten zijn niet gelijk")


meubels = {'banken': 10, 'stoelen': 20}
meubels ['banken'] += 6
print (meubels)
meubels = {'banken': 10, 'stoelen': 20}
meubels.update(banken = 4)
print (meubels)
del meubels['stoelen']
print (meubels)
meubels ["Tafels"] = 15
print (meubels)


cijfers = {'Jaap': 3, 'Winnie': 4, 'Jeroen': 9, 'Lana': 10, 'Herman': 6.7}
print (cijfers)
for naam, grade in cijfers.items():
    if grade * 1.5 > 10:
        cijfers[naam] = 10
    else:
        cijfers[naam] = grade * 1.5

print (cijfers)


dieren = {'Olifant': 5, 'Zebra': 8, 'Aap': 12, 'Giraffe': 3, 'Neushoorn': 7}
for dier, aantal in sorted(dieren.items()):

    print (dier,":", aantal, end=', ')
print ()
for aantal in sorted(dieren.values(),reverse=True):
    print(dier, ":", aantal, end=', ')
