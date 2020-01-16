class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n - 1) + self.climbStairs(n - 2)

    def climbStairsDp(self, n, dp):
        if n == 1:
            return 1
        if n == 2:
            return 2
        if not dp[n]:
            dp[n] = self.climbStairsDp(n - 1, dp) + self.climbStairsDp(n - 2,
                                                                       dp)
        return dp[n]

    def climbStairsLoop(self, n):
        if n == 1 or n == 2:
            return n
        temp1 = 1
        temp2 = 2
        result = 0
        for i in range(3, n + 1):
            result = temp1 + temp2
            temp1 = temp2
            temp2 = result
        return result

    def climbStairsLoopMajor(self, n):
        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        return b


if __name__ == "__main__":
    n = 1
    dp = [None] * (n + 1)
    s = Solution()
    print(s.climbStairs(n))
    print(s.climbStairsDp(n, dp))
    print(s.climbStairsLoop(n))
    print(s.climbStairsLoopMajor(n))
