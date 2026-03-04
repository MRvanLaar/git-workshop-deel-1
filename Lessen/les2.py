num1 = 30
num2 = 20
num3 = 10

a = (num3,num2,num1)
#dit is een comment

'''
CTRL+/ maakt iets een comment
'''
numbers = sorted(a)
print(numbers)

x = 6

match x:
    case 1: print("maandag")
    case 2: print("Dinsdag")
    case 3: print("Woensdag")
    case _: print("Andere dag")

x = 6
if x % 2 == 0:
    print("dit is even")
elif x % 2 == 1:
    print("dit is oneven")
elif x % 3 == 0:
    print("dit is deelbaar door 3")
else:
    print("dit is een float")

tf = ""

if not tf:
    print("dit wordt altijd geprint")

# else if statements
oppervlakte = 350
ruimtes = 4
prijs = 2000

if (prijs < 2000) and (ruimtes > 3) and (oppervlakte > 30):
    print("Dit is interessant")
elif prijs > 2000 and ruimtes > 3 and oppervlakte > 100:
    print("erg dur, maar het overwegen waard vanwege de oppervlakte")
elif prijs > 2000 and ruimtes > 3 and oppervlakte > 30:
    print("dit is te duur")

elif ruimtes < 3 :
    print("Ik heb 12 kinderen, dus dit is te klein")
else:
    print("Check even je gegevens, want er klopt iets niet")

# Alternatief voor If then else
x = 5
match x:
    case 1: print("Maandag")
    case 2: print("Dinsdag")
    case 3: print("Woensdag")
    case 4|5: print("Donderdag")
    case _: print("Andere dag")


# infinate loops doorbreken
x = 10
keep_going = x < 15

while keep_going:
    print(f"keep going {x}")
    x += 1
    keep_going = x < 15

running = true

