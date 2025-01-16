test_list = [1, 2, 3, 4, 5]
for i in test_list:
    print(i)

a = range(10)
print(a)

add = 0
for i in range(1, 11):
    add += i
print(add)

a = [1, 2, 3, 4]
result = []
for num in a:
    result.append(num * 3)
print(result)

result2 = [num * 3 for num in a]
print(result2)