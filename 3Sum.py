class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        sortedNums = sorted(nums)
        i = 0
        print(sortedNums)
        while i < len(sortedNums):
            # do two sum with two pointers j and k on the rest of the list
            target = -1 * sortedNums[i]
            j = i + 1
            k = len(sortedNums) - 1
            while j < k:
                if target == sortedNums[j] + sortedNums[k]:
                    result.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    # move j to the next strictly bigger number
                    j = bisect_right(sortedNums, sortedNums[j], j + 1)
                elif sortedNums[j] + sortedNums[k] > target:
                    k -= 1
                elif sortedNums[j] + sortedNums[k] < target:
                    j += 1
            # skip duplicate numbers for i
            i = bisect_right(sortedNums, sortedNums[i], i + 1)
        return result
