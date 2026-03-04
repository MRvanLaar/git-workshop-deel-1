print("Welkom, bij pizzaday.")
grootte_1 = input("Kies nu je pizza grootte: small, medium of large." )
Keuze2 = input("wil je extra pepporoni? Ja of nee")
Keuze3 = input("wil je extra kaas? Ja of nee")

if grootte_1 == "small":
    rekening_1 = 10
    if Keuze2 == "ja".lower():
        rekening_1 += 2
elif grootte_1 == "medium":
    rekening_1 = 12
    if Keuze2 == "ja".lower():
        rekening_1 +=2
elif grootte_1 == "large":
    rekening_1 = 14
    if Keuze2 == "ja".lower():
        rekening_1 += 2
if Keuze3 == "ja":
    rekening_1 += 1

print(f"de totale kosten van uw pizza zijn: {rekening_1}")
