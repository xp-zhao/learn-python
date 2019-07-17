d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])

# 判断 key 是否存在于字典中
print('Thomas' in d)
print(d.get('Thomas'))
print(d.get('Thomas', -1))

# 删除一个 key
print(d)
print(d.pop('Bob'))
print(d)