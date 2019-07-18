filepath = "D:\\code\\python\\learn-python\\io\\test.txt"

try:
    with open(filepath) as file_object:
        for line in file_object:
            print(line.rstrip())
except FileNotFoundError:
    print("sorry, the file does not exist")

with open('programming', 'w') as file_object:
    file_object.write("I love programming")