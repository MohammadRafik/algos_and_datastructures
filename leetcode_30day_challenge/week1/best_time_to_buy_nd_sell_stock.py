class Solution:
    def maxProfit(self, prices) -> int:
        sum = 0
        for i in range(len(prices)-1):
            dif = prices[i+1]-prices[i]
            if 0 < dif:
                sum += dif
        return sum