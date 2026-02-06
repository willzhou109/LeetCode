class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = 0
        best = 0
        for r in range(0, len(prices)):
            profit = prices[r] - prices[l]
            while profit < 0:
                l += 1
                profit = prices[r] - prices[l]
            best = max(best, profit)
        return best
