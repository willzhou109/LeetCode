class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        prefix = list(range(len(height)))
        suffix = list(range(len(height)))
        for i in range(len(height)):
            if i == 0:
                prefix[i] = height[i]
            else:
                prefix[i] = max(prefix[i - 1], height[i])
        for i in range(len(height) - 1, -1, -1):
            if i == len(height) - 1:
                suffix[i] = height[i]
            else:
                suffix[i] = max(suffix[i + 1], height[i])
        
        # determine water level at each position in the array
        total_water = 0
        for i in range(len(height)):
            water = min(prefix[i], suffix[i]) - height[i]
            total_water += water
        return total_water