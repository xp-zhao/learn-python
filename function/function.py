import math
# 求绝对值的函数
def my_abs(x):
    if not isinstance(x, (int, float)):
        raise TypeError('bad operand type')
    if x >= 0:
        return x
    else:
        return -x

# 求一元二次方程解的函数
def quadratic(a, b, c):
    r1 = (-b + math.sqrt(b * b - 4*a*c)) / (2*a)
    r2 = (-b - math.sqrt(b ** 2 - 4*a*c)) / (2*a)
    return r1, r2

print('quadratic(2, 3, 1) =', quadratic(2, 3, 1))
print('quadratic(1, 3, -4) =', quadratic(1, 3, -4))
if quadratic(2, 3, 1) != (-0.5, -1.0):
    print('测试失败')
elif quadratic(1, 3, -4) != (1.0, -4.0):
    print('测试失败')
else:
    print('测试成功')

# 默认参数 (默认参数必须指向不变对象)
def power(x, n=2):
    s = 1
    while n > 0:
        n = n - 1
        s = s * x
    return s
print(power(6))
print(power(6, 3))

# 可变参数
def calc(*nums):
    sum = 0
    for n in nums:
        sum = sum + n * n
    return sum
print(calc(1, 2, 3))
print(calc(1, 2, 3, 4))
print(calc())
print(calc(*[1,2,3])) # * 号表示将 list 的所有元素当可变参数传递进去

# 关键字参数
def person(name, age, **kv):
    print('name:', name, 'age:', age, 'other:', kv)
person('Michael', 30)
person('Michael', 30, city='Beijing')
extra = {'city': 'Beijing', 'job': 'Engineer'}
person('Michael', 30, **extra)

# 递归函数
def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
print(fact(5))