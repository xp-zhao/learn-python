def triangles(m):
    a = [1]
    while len(a) <= m:
        yield a
        b = a[:]
        for i in range(1, len(a)):
            b[i] = a[i - 1] + a[i]
        b.append(1)
        a = b


for n in triangles(2):
    print(n)
