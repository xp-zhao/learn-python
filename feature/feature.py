# 切片
strs = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']
print(strs[0:3]) # 取前三个元素
print(strs[:3])

nums = list(range(100))
print(nums[:10]) # 取前十个数
print(nums[-10:]) # 取后十个数
print(nums[10:20]) # 取前 11-20 个数
print(nums[:10:2]) # 前十个数，每两个取一个
print(nums[::5]) # 所有数，每五个取一个

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key in d:
    print(key)
for value in d.values():
    print(value)
for k, v in d.items():
    print(k, v)

# 列表生成式
print(list(range(1,11)))
print([x * x for x in range(1, 11)])
print([x * x for x in range(1, 11) if x % 2 == 0])
print([m + n for m in 'ABC' for n in 'XYZ'])
L = ['Hello', 'World', 'IBM', 'Apple']
print([s.lower() for s in L])

# 生成器
g = (x * x for x in range(10))
for n in g:
    print(n)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'
for n in fib(6):
    print(n)