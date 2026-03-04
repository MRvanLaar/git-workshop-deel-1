kleuren = {'rood', 'blauw', 'geel'} # Set worden aangeven met {} deze waarden komen maar een keer voor

print (kleuren)
print(type(kleuren), kleuren)

lege_verzameling = set()
print("lege verzameling:", type(lege_verzameling))

leeg_woordenboek = {}
print("leeg woordenboek:", type(leeg_woordenboek))

getallen = set(range(0,11)) # range aangeven in een set.
print(type(getallen), getallen)

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'blauw', 'geel', 'rood'}
print('gelijk' if kleuren1 == kleuren2 else 'niet gelijk') # andere manier van If else statement

kleuren = {'rood', 'blauw', 'geel', 'blauw'} # waarden worden maar 1x weergegeven.
print(sorted(kleuren))

kleuren = {'rood', 'blauw', 'geel'}
print('geel', 'geel' in kleuren)
print('wit', 'wit' in kleuren)
print('oranje', 'oranje' not in kleuren)

kleuren = {'rood', 'blauw', 'geel'}
print('aantal elementen :', len(kleuren)) # aantal items weergeven in een set

kleuren = {'rood', 'blauw', 'geel'}
kleuren.add('wit') # toevoegen aan een set
print(kleuren)

kleuren.remove('blauw') # verwijderen uit een set
print(kleuren)

if 'oranje' in kleuren:
    kleuren.remove('oranje')
else:
    kleuren.add('oranje')
print(kleuren)

kleuren = {'rood', 'blauw', 'geel'}
kleuren.clear()
print(kleuren)

kleuren = {'rood', 'blauw', 'geel'}


for kleur in kleuren :
    print(kleur.upper(), end = '; ')
print ()

kleuren = frozenset({'rood', 'blauw', 'geel'}) # dit kan je niet muteren. Handig voor vaste waarden/items
print(kleuren)

getallen = [1, 2, 2, 3, 4, 5, 6, 6, 7, 8, 9, 10, 10]
even_getallen = {getal for getal in getallen if getal % 2 == 0}
print(even_getallen)

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'geel', 'rood'}
print(kleuren2 <= kleuren1) # geeft zelfde aan als hieronder. kijkt of kleuren 2 onderdeel is van kleuren 1
print(kleuren2.issubset(kleuren1))
print(kleuren2.issuperset(kleuren1))

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'wit', 'geel', 'oranje', 'rood'}
kleuren3 = kleuren1 | kleuren2 # sets samenvoegen doe je met | IPV + icoon Join
kleuren4 = kleuren1.union(kleuren2) # Zelfde als hierboven
print(kleuren3)
print(kleuren4)
kleuren5 = kleuren1 & kleuren2 # inner join (alleen overlappende items worden geshowed
print (kleuren5)


kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2_tupel = ('wit', 'geel', 'oranje', 'rood')
kleuren3 = kleuren1.intersection(kleuren2_tupel) # inner join met tupel (alleen overlappende items worden geshowed
print(kleuren3)

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'wit', 'geel', 'oranje', 'rood'}
kleuren3 = kleuren1 - kleuren2 # outer join, laat alleen de items zien die niet overeen komen (Delta)
kleuren4 = kleuren1.difference(kleuren2) # outer join, laat alleen de items zien die niet overeen komen (Delta) kan ook met niet sets
print(kleuren3)
print(kleuren4)

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'wit', 'geel', 'oranje', 'rood'}
kleuren3 = kleuren1 ^ kleuren2 # items die niet in elkaars bronnen staan.
print(kleuren3)

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'wit', 'geel', 'oranje', 'rood'}
kleuren1 |= kleuren2 # komt in een van de bronnen voor
print(kleuren1)

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'wit', 'geel', 'oranje', 'rood'}
kleuren1 &= kleuren2 # voegt de bronnen samen
print(kleuren1)

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'wit', 'geel', 'oranje', 'rood'}
kleuren1 -= kleuren2 # trekt de bronnen van elkaar af aan een kant.
print(kleuren1)

kleuren1 = {'rood', 'blauw', 'geel'}
kleuren2 = {'wit', 'geel', 'oranje', 'rood'}
kleuren2 ^= kleuren1
print(kleuren2)


