from operator import index

numbers = [2, 5, 7, 11, 15, 16,22]
print (numbers)
print (type(numbers))

print (numbers[-2]) # print specifiek nummer van achteren, handig om de laatste te selecteren
aantal = (len(numbers)-1)
print (numbers [4]) # print specifiek nummer van voren, handig als je de eerste wil overslaan, kan nooit meer zijn dan aantal numbers
print (numbers [aantal])

numbers.append(3)
numbers.extend([19,21,26])
numbers.insert(3,14)
numbers_sorted = sorted(numbers)
print (numbers_sorted)
print (numbers_sorted [1:8]) # specifieke lijst Slicing
print (numbers_sorted [:8]) # specifiek aantal nummers van achteren Slicing
print (numbers_sorted [8:]) # specifiek aantal nummers van voren Slicing
print (numbers_sorted [::2]) # gesorteerd van voren met stappen van 2 Slicing
print (numbers_sorted [::-2]) # gesorteerd van achteren met stappen van 2 Slicing
print (numbers_sorted [1:8:2]) # 1 eerste nummer, 8 Laatste nummer op positie 8, 2 aantal tussenstappen. Slicing

# uitgeschreven hoe iets te verwijderen/toe te voegen
namen = ['Alfred', 'Bob', 'Charlie', 'David', 'Erik']
namen.remove("David")
namen.remove("Erik")
namen.insert(3, "Daphne")
namen.insert(4, "Eva")
namen.insert(5, "Frederieke")
print(namen)
print(namen [-1][0]) # laatste woord uit de lijst, eerste letter.

#verkort van het bovenstaande
namen = ['Alfred', 'Bob', 'Charlie', 'David', 'Erik']
print(namen)
print(namen[0:3])
namen[3:5] = ("Daphne", "Eva", "Frederieke")
print(namen)
