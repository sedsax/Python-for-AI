numbers = []

numbers = [i for i in range(100) if i % 3 == 0 if i %4 == 0]
print(numbers)

numbers = [i for i in range(1, 100) if i % 12 == 0]
print(numbers)

text = "Hello 12345 World"
numbers = [int(i) for i in text if i.isdigit()]
#print(numbers)
numbers = [i for i in text if i.isdigit()]
#print(numbers)
numbers = [int(i)*2 for i in text if i.isdigit()]
#print(numbers)
numbers = [i*2 for i in text if i.isdigit()]
#print(numbers)
 
students = ["Ali", "Veli", "Canan"]
notes = [70, 80, 90]
student_notes = {student: note for student, note in zip(students, notes)}
#print(student_notes)
student_notes = {student: note for student, note in zip(students, notes) if note > 80}
#print(student_notes)
student_notes = {student: note if note > 80 else "Kaldi" for student, note in zip(students, notes)}
#print(student_notes)
student_notes = [(students[i], notes[i]) for i in range(len(students))]
#print(student_notes)
#student_notes = {student: note for student, note in student_notes}
#print(student_notes)
student_notes_dict = {key:value for (key, value) in student_notes if value > 80}
#student_notes = {student: note for student, note in student_notes if note > 70}
print(student_notes_dict)

sonuc = []
for x in range(3):
    for y in range(3):
        for z in range(3):
            sonuc.append((x, y, z))
            print(x, y, z)

print(sonuc)

sonuc = [(x, y, z) for x in range(3) for y in range(3) for z in range(3)]
print(sonuc)