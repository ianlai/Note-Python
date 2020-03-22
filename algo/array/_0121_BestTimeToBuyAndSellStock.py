class Solution:
    
    # Brute force, O(n2)
    def maxProfit_BruteForce(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        maxRevenue = 0 
        for i in range(len(prices)):
            revenue = max(prices[i:]) - prices[i]
            maxRevenue = max(revenue, maxRevenue)
        return maxRevenue
    
    # Two Variables, O(n)
    def maxProfit(self, prices: List[int]) -> int:
        if len(prices) == 0:
            return 0
        
        minPrice = float('inf')
        maxProfit = 0
        
        for i in range(len(prices)):
            minPrice = min(prices[i], minPrice)
            maxProfit = max(prices[i] - minPrice, maxProfit)
        return maxProfit