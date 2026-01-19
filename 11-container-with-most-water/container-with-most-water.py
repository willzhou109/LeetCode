class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        curr_max = 0
        l = 0
        r = len(height) - 1
        while l < r:
            area = min(height[l], height[r]) * (r - l)
            if area > curr_max:
                curr_max = area
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        return curr_max 