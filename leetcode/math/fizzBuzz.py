import leetcode.recursion.recursion as re

class Solution:
    def fizzBuzz(self, n: int) -> list:
        str_list = []
        a = "Fizz"
        b = "Buzz"
        for i in range(1, n + 1):
            if i % 3 == 0 and i % 5 == 0:
                str_list.append(a + b)
            elif i % 3 == 0:
                str_list.append(a)
            elif i % 5 == 0:
                str_list.append(b)
            else:
                str_list.append(i)
        return str_list


if __name__ == '__main__':
    s = Solution()
    print(s.fizzBuzz(15))
    re.f_1(10)
