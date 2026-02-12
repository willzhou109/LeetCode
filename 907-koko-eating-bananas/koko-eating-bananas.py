import math


class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        hi = max(piles) # max eating speed (bananas/hour)
        lo = 1 # min eating speed (bananas/hour)
        while hi >= lo:
            k = (hi + lo) / 2
            time = 0
            for n in piles:
                if n % k == 0:
                    time += n / k
                else:
                    time += (n / k) + 1
            print("high: " + str(hi) + " low: " + str(lo) + " k: " + str(k) + " time: " + str(time))
            if time <= h: # ate too fast or equal to
                hi = k - 1
            else: # ate too slow
                lo = k + 1
           
        return lo