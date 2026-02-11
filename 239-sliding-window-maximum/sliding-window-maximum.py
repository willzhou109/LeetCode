from collections import deque


class Solution(object):
    def maxSlidingWindow(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        l = 0
        dq = deque() # consists of indices
        output = []


        for r in range(0, len(nums)):
            while dq and nums[dq[-1]] <= nums[r]: # while deque is not empty and rightmost element is smaller or equal to current
                dq.pop()
            else: # deque is empty or current element is smaller than rightmost of deque
                dq.append(r)
            if r == l + k - 1:
                output.append(nums[dq[0]]) # append leftmost element of the deque to the output, this will be the max of that window
                l += 1
                if dq and l > dq[0]: # if the new window no longer contains the maximum
                    dq.popleft()
            r += 1
       
        return output
