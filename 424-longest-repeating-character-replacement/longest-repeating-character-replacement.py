class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        l = 0
        maxLen = 0
        ht = defaultdict(int) # records the key as the letter, and value as the number of occurances in the subarray between l and r
        maxCount = 0 # number of occurances of the most frequent character within the given window
        for r in range(0, len(s)):
            length = r - l + 1
            ht[s[r]] += 1
            maxCount = max(maxCount, ht[s[r]]) # update the current most popular letter if it gets surpassed
            num_to_replace = length - maxCount
            while num_to_replace > k: # resize the window from the left
                ht[s[l]] -= 1
                l += 1
                length = r - l + 1
                num_to_replace = length - maxCount
            maxLen = max(maxLen, length)
        return maxLen