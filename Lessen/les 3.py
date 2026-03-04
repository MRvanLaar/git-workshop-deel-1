boodschappen = ["boter", "beschuit", "pizza", "augurk", "pindakaas"]
print (boodschappen[0], "&", boodschappen[2])
print (boodschappen [1:4])


coord = (156, 763)
lijst_van_coordinaten = [(123, 234), (235, 562), (564, 762), (156, 763)]

print ("x:",coord[0], "Y: ", coord[1])
print ("x:",lijst_van_coordinaten[1][0], "Y: ", lijst_van_coordinaten[1][1])

studenten = [("Alice", 8.5), ("Bob", 7.0), ("Charlie", 6.2), ("Diana", 9.1)]
total = 0
highest_student_grade = []
prev_student_grade = 0

print("Studenten en hun cijfers:")
for name, grade in studenten:
    total += grade
    print(name, grade)

    if prev_student_grade < grade:
        highest_student_grade.insert(0, name)
        highest_student_grade.insert(1, grade)
    prev_student_grade = grade


average = round(total / len(studenten), 1)
print(f"\nGemiddelde score: {average}")
print(f"De beste student is {highest_student_grade[0]} met een {highest_student_grade[1]}!")