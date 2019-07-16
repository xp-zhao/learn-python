list = []
list.append(1)
list.append("xp")
list.append(2)
print(list)

list.insert(0, 'hj')
print(list)

for value in range(1,5):
    print(value)

squares = []
for value in range(1,11):
    squares.append(value ** 2)
print(squares)

# 对数字列表进行简单统计
num = [1,2,3,4,5,6]
print(min(num))
print(max(num))
print(sum(num))

# 列表解析
list1 = [value ** 2 for value in range(1, 11)]
print(list1)

# 元组，和列表操作一致 但不可修改
temp = (200, 50)
print(temp[0])
print(temp[1])