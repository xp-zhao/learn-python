# 数字分隔符
def declare_data():
    a = 10_0000_0000
    print(a)

# 交换变量值
def replace_var():
    a = 1
    b = 2
    print(a, b)
    a, b = b, a
    print(a, b)

# 连续比较式
def compare():
    a = 10
    print(1 <= a <= 10)

# 字符串乘法
def str_multi():
    print('_' * 3)

# 列表拼接
def list_add():
    a = [1, 2, 3]
    b = [4, 5, 6]
    c = a + b
    print(c)

# 列表切片
def list_split():
    a = [1, 2, 3]
    print(a[-1])

# 打包解包
def pack_unpack():
    a = [1, 2, 3]
    x, y, z = a
    print(x, y, z)

# 列表推导式
def list_cal():
    a = [1, 2, 3]
    b = [i*i for i in a]
    print(b)

if __name__ == '__main__':
    declare_data()
    replace_var()
    list_add()
    list_split()
    pack_unpack()
    compare()
    str_multi()
    list_cal()
