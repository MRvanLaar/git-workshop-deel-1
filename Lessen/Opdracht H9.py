getallen = {1, 2, 3}

getallen.add(1)
getallen.add(4)

print('getallen: ', getallen)  # Het resultaat is: {1, 2, 3, 4}

verzameling = {3, 44, 17, 23, 58, 9, 36}
verzameling.add (27)
verzameling.remove(23)
print (verzameling)

for verz in verzameling:
    if verz > 20 and verz < 50 :
        print(verz, end=', ')
print()

verzameling_kleuren_1 = {'red', 'blue', 'green'}
verzameling_kleuren_2 = {'yellow', 'blue', 'green'}
vergelijk1 = verzameling_kleuren_1.difference(verzameling_kleuren_2)
print(vergelijk1)
vergelijk2 = verzameling_kleuren_1 ^ verzameling_kleuren_2
print(vergelijk2)
vergelijk3 = verzameling_kleuren_1.symmetric_difference(verzameling_kleuren_2)
print(vergelijk3)


verzameling1 = {11, 22, 33}
verzameling2 = {5, 11, 16, 22}
print (verzameling1 - verzameling2)
print (verzameling2 - verzameling1)
print (verzameling1 | verzameling2)
print (verzameling1 & verzameling2)
