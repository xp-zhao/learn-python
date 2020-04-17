# file1 = open("name.txt", 'w', encoding='utf-8')
# file1.write("诸葛亮")
# file1.close()
#
# file2 = open("name.txt", encoding='utf-8')
# print(file2.read())
# file2.close()
#
# file3 = open("name.txt", 'a', encoding='utf-8')
# file3.write("刘备")
# file3.close()

# file4 = open("name.txt", encoding="utf-8")
# print(file4.readline())
#
# file5 = open("name.txt", encoding="utf-8")
# for line in file5.readlines():
#     print(line)
#     print("====")

file6 = open("name.txt", encoding='utf-8')
print('当前文件指针的位置 %s' % file6.tell())
print('当前读取到的值 %s' % file6.read(1))
print('当前文件指针的位置 %s' % file6.tell())
file6.seek(0)
print('当前文件指针的位置 %s' % file6.tell())
print('当前读取到的值 %s' % file6.read(1))
print('当前文件指针的位置 %s' % file6.tell())
