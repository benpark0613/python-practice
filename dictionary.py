dic1 = {'name': 'ben', 'tel': '010-1234-5678', 'age': 20}
print(dic1['name'])
print(dic1['tel'])
print(dic1['age'])
del dic1['name']
print(dic1)

a = {(1,2): 'test', (2,3): 'test2'}
print(a[(1,2)])


dic2 = {'name': 'ben', 'tel': '010-1234-5678', 'age': 20}
print(dic2.keys())
print(dic2.values())

for k in dic2.keys():
    print(k)

print(dic2['name'])
print(dic2.get('name'))
print(dic2.get('pet', 'not found'))

print('tool' in dic2)