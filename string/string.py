# title() 方法，以首字母大写的方式显示每个单词
name = "ada lovelace"
print(name.title())

# 字符串大小写转换
print(name.upper())
print(name.lower())

# 字符串合并
first_name = "ada"
last_name = "lovelace"
full_name = first_name + " " + last_name
print(full_name)
print("hello, " + full_name.title() + "!")

# 空白处理
string = "\tpython\t"
print(string)
print(string.rstrip())
print(string.lstrip())