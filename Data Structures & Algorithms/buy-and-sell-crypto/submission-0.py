class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i, j = 0, 1
        n = len(prices)
        result = 0
        while i < n - 1 and j < n:
            if prices[j] <= prices[i]:
                i, j = j, j + 1
                continue
            result = max(result, prices[j] - prices[i])
            j += 1
        return result