class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) < 2:
            return 0
        l, r = 0, 1 
        result = 0 
        minBuy, maxSell = prices[l], prices[r]
        curr = result
            
        while r < len(prices):
            if prices[r] < prices[l]:
                l = r
            else:
               curr = prices[r] - prices[l]
            r += 1
            result = max(result, curr)

        return result
        