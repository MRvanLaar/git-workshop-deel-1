jouw_naam = "Mike"
vriends_naam = "Daan"
sport = "Volleybal"
boom_soort = "Eik"

verhaal = (f" Er was een een Koning genaamd {jouw_naam}. "
        f"Hij reageerde met zijn rechterhand genaamt {vriends_naam}. "
        f"Samen speelde ze {sport}. "
        f"Dit deden ze vaak bij de oude {boom_soort}.")

print(verhaal)

print ("")
print("Nu maken verhaal specail voor jou, vul de vragen in")
jouw_naam = input ("Wat is je naam? ")
Vriends_naam = input ("Wat is je vriends naam? ")
sport = input ("Welke sport speel je? ")
boom_soort = input ("Wat is je favoriere boomsoort? ")

verhaal = (f"Er was een een Koning genaamd {jouw_naam}. \n"
        f"Hij reageerde met zijn rechterhand genaamt {vriends_naam}. \n"
        f"Samen speelde ze {sport}. \n"
        f"Dit deden ze vaak bij de oude {boom_soort}.\n")

print (verhaal)