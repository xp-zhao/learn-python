class Solution:
    def maxProfit(self, prices: list) -> int:
        min_price = max(prices) + 1
        max_price = 0
        for num in prices:
            if num < min_price:
                min_price = num
            elif num - min_price > max_price:
                max_price = num - min_price
        return max_price


if __name__ == "__main__":
    prices_list = [7, 1, 5, 3, 6, 4]
    s = Solution()
    print(s.maxProfit(prices_list))
