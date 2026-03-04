totaal = 0
aantal_getallen = 0

getal = int(input("Voer een getal in:\n"))

while getal != 0:
    totaal += getal
    aantal_getallen += 1
    getal = int(input("Voer een getal in:\n"))
if aantal_getallen != 0:
    print ("Totaal",totaal)
    print ("Aantal", aantal_getallen)
    print ("Gemiddelde", totaal/aantal_getallen)
else:
    Print ("Er zijn geen getallen ingevoerd")

