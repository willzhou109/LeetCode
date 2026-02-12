class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        l = 0
        maxLen = 0
        hash_set = set()
        for r in range(0, len(s)):
            while s[r] in hash_set: # duplicate exists
                hash_set.remove(s[l])
                l += 1
            maxLen = max(maxLen, r - l + 1)
            hash_set.add(s[r])
            r += 1
        return maxLen