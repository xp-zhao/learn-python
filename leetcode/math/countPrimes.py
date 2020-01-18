class Solution:
    def countPrimes(self, n: int) -> int:
        count = 0

        def isPrimes(num):

            for i in range(2, num):
                if num % i == 0:
                    return False
            return True

        for i in range(2, n):
            if isPrimes(i):
                count += 1
        return count


if __name__ == '__main__':
    s = Solution()
    print(s.countPrimes(10))
