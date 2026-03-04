vakken = {'Python':10, 'Java':8, 'C#':5}
print(type(vakken), vakken)

vakken = {'Python':10, 'Java':8, 'C#':5}

print('Python', 'Python' in vakken) # zoeken of iets waar is
print('SQL', 'SQL' in vakken) # zoeken of iets waar is
print('Pascal', 'Pascal' not in vakken) # zoeken of iets waar is

vakken = {'Python': 10, 'Java': 8, 'C#': 5, 'SQL': 6}

print(vakken.get('Pascal', 'Pascal staat niet in het woordenboek'))
print(vakken.get('Java', 'Java staat niet in het woordenboek'))


vakken = {'Python': 10, 'Java': 8, 'C#': 5, 'SQL': 6}
vakken['Pascal'] = 4 # toevoegen van items aan een woordenboek
del vakken['C#'] # verwijderen van items aan een woordenboek
vakken.update(Java = 7) # toevoegen en updaten van items
print(vakken)

vakken = {'Python': 10, 'Java': 8, 'C#': 5, 'SQL': 6, 'Pascal': 4}

for vak,aantal in vakken.items() :

    if aantal <= 6 :

        print(vak, '->', aantal)

vakken = {'Python': 10, 'Java': 8, 'C#': 5, 'SQL': 6, 'Pascal': 4}

for vak in sorted(vakken.keys()) :

    print(vak, end='')

vakken = {'Python': 10, 'Java': 8, 'C#': 5, 'SQL': 6}

vakken_view = vakken.keys()
vakken_view2 = vakken.values()

print(vakken_view)

vakken['Pascal'] = 4

print(vakken_view)
print(vakken_view2)

cijfers = {'Jan': [7.3, 8.5, 6.4], 'Piet': [6.9, 7.2, 9.1, 8.1]}

gemiddelde_cijfers = {s : sum(w) / len(w) for s, w in cijfers.items()}

print(gemiddelde_cijfers)
