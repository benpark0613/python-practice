# f = open("test.txt", "w")
# for i in range(1, 11):
#     data = "%d번째 줄\n" % i
#     f.write(data)
# f.close()

with open("test.txt", "w") as f:
    f.write("Hello World!")

with open("test.txt", "r") as f:
    print(f.read())