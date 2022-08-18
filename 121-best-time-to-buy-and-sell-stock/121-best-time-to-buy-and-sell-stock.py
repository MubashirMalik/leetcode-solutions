class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_current = 0
        max_global = max_current
        min_buy = prices[0]
        
        for _, price in enumerate(prices):
            if price <= min_buy:
                min_buy = price
            else:
                max_current = price - min_buy
            
            if max_current > max_global:
                max_global = max_current
        
        return max_global
            
        