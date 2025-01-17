from operator import itemgetter

students = [
    ("jane", 22, 'A'),
    ("john", 21, 'B'),
    ("jim", 24, 'A'),
]

result = sorted(students, key=itemgetter(1))
print(result)