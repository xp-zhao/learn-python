# try:
#     year = int(input('input year:'))
# except ValueError:
#     print("年份要输入数字")

# try:
#     print(1 / 0)
# except ZeroDivisionError as e:
#     print("0不能做除数 %s" % e)
#
# try:
#     raise NameError("helloError")
# except NameError:
#     print("my custom error")

try:
    a = open("name.txt")
except Exception as e:
    print(e)
finally:
    a.close()