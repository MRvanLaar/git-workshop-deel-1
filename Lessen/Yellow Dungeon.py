'''
print("Welkom in de dungeon. Waar wil je heen? \n Kies een deur:")
keuze = input("Kies blauw, geel of groen\n").lower()
while not (keuze == "blauw" or keuze == "geel" or keuze == "groen"):
    print("kies een geldig antwoord")
    keuze = input("Kies blauw, geel of groen\n")
if keuze == "blauw":
    print("Je ziet een meer, ga je door de rode deur of de grone deur?")
    keuze2 = input("kies groen of rood")
    if keuze2 == "groen":
        print("Er springt een monster uit het water en eet je op!\nJe hebt verloren!")
    else:
        print("Je komt in een rode kamer en ziet de finish. Je open de deur en je bent weer buiten.\nGefeliciteerd!")

'''

# Dungeon application: Deze applicatie is een "choose your own adventure" verhaal. Gebaseerd op If-else statements en while loops. Zie 'if-else-dungeon' document voor een transcriptie van het verhaal.

print("Goeiemorgen!\nHet is 8 uur\nVandaag is een drukke dag, moet naar je werk.\nWat doe je als eerst?\n")
keuze = input("kies opstaan of snoozen\n").lower()
while not (keuze == "opstaan" or keuze == "snoozen"):
    print("Wat doe je?\n")
    keuze = input("kies uit opstaan of snoozen").lower()
if keuze == "opstaan":
    print("Je staat op.\nWat doe je nu?\n")
    keuze_2 = input("Kies uit douchen, de hond uit laten of ontbijten:\n").lower()
    if keuze_2 == "douchen":
        print(
            "je doucht je ruikt lekker, maar je hebt geen tijd meer om te eten.\nJe komt zo te laat.\nWat doe je nu?\n")
        keuze_3 = input("Kies om toch te eten, of je naar je werk te gaan.").lower()
        if keuze_3 == "werk":
            print("Je komt op tijd op je werk, maar je hebt heel de dag honger dus je presteert niet zo goed.")
        elif keuze_3 == "eten":
            print("Je komt te laat op je werk, je baas is boos, je bent ontslagen.")
        else:
            print("Dit is geen juiste keuze")
else:
    print("Je valt weer in slaap, je wordt wakker om 10 uur.\nJe bent te laat op je werk, je bent helaas ontslagen.")

# De fiets-motivator

# Geef aan welk weer het is
keuze = input("Wat is het weer? \n Kies uit zon, regen of anders : ")
while not (keuze == "zon" or keuze == "regen" or keuze == "anders"):
    print("Je hebt geen correcte keuze gemaakt")
    keuze = input("Wat is het weer? \n Kies uit zon, regen of anders : ")
# De opties als de zon schijnt
if keuze == "zon":
    print("Het is lekker weer!")
    keuze2 = input("Pak je de fiets of de auto? ")
    if keuze2 == "fiets":
        print("Goed bezig! Je werkt aan je gezondheid")
    elif keuze2 == "auto":
        print("Je hebt Frans Timmermans boos gemaakt")
