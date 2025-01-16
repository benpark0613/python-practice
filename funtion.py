def sub(a, b):
    return a - b

result = sub(b = 20, a = 10)
print(result)

def add_many(*args):
    result = 0
    for i in args:
        result += i
    return result

result = add_many(1, 2, 3, 4, 5)
print(result)

def print_kwargs(**kwargs):
    print(kwargs)

print_kwargs(a = 1)
print_kwargs(name ='foo', age = 20)

def add_and_mul(a, b):
    return a + b, a * b

result = add_and_mul(1, 2)
print(result)

add = lambda a, b: a + b
result = add(1, 2)
print(result)