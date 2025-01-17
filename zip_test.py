names = ['a', 'b', 'c']
scores = [1, 2, 3]

result = zip(names, scores)
print(list(result))

for name, score in zip(names, scores):
    print(f"{name}: {score}")