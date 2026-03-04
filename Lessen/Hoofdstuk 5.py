from functools import total_ordering

basisprijs = 12
peuter = 5
jeugd = 12
ouderen = 55

korting_peuter = 0.0
korting_jeugd = 0.5
korting_ouderen = 0.0

leeftijd = input("Voer je leeftijd in:\n")

while leeftijd.isnumeric() == False:
    print("Vul een getal in.")
    leeftijd = input("Voer je leeftijd in:\n")

leeftijd = int(leeftijd)

if leeftijd <= peuter:
    print("Uw prijs €", korting_peuter * basisprijs)
elif leeftijd <= jeugd:
    print("Uw prijs €", korting_jeugd * basisprijs)
elif leeftijd >= ouderen:
    print("Uw prijs €", korting_ouderen * basisprijs)
else:
    print("Uw prijs €", basisprijs)
