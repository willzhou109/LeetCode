class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = 0
        r = len(nums) - 1
        while l <= r:
            m = (l + r) / 2
            if nums[l] <= nums[r]:
                return nums[l]
            else:
                if nums[l] <= nums[m]:
                    l = m + 1
                elif nums[r] >= nums[m]:
                    r = m
