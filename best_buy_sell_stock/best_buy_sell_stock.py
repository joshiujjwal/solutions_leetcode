class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        max_profit = 0
        min_price = sys.maxsize
        
        for i in prices:
            if i < min_price:
                min_price = i
            else:
                if i - min_price > max_profit:
                    max_profit = i - min_price
                    
        return max_profit
        
