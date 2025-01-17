import itertools

students = ['Alice', 'Bob', 'Charlie', 'David', 'Eve']
snacks = ['Python', 'Ruby', 'PHP']

result = itertools.zip_longest(students, snacks, fillvalue='c')
print(list(result))