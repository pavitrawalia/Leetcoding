class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minPrice, result = prices[0], 0
        for i in range(1, len(prices)):
            minPrice = min(minPrice, prices[i])
            result = max(result, prices[i] - minPrice)
        return result
                
