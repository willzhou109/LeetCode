class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        l = 0
        min_len = len(s)
        r_min = -1
        l_min = -1 # r and l which the minimum length substring was found
        freq_t = defaultdict(int) # hashmap representing frequencies of characters in t
        freq_s = defaultdict(int) # hashmap representing frequencies of characters in current window
        curr_valid_chars = 0 # current number of valid characters (characters that are in t) in the window

        # populate the t dictionary
        for i in range(0, len(t)):
            freq_t[t[i]] += 1
            
        for r in range(0, len(s)):
            freq_s[s[r]] += 1
            if s[r] in freq_t and freq_s[s[r]] <= freq_t[s[r]]: # if found a valid char that wasn't already in the window
                curr_valid_chars += 1
            # print("1 " + " l: " + str(l) + " r: " + str(r) + " window: "+ str(s[l:(r+1)]) + " curr_valid: " + str(curr_valid_chars))
            while curr_valid_chars == len(t): # if the current window is satisfactory, shrink it from the left
                if r - l + 1 <= min_len:
                    r_min = r
                    l_min = l
                min_len = min(min_len, r - l + 1)
                #print("l_min: " + str(l_min) + " r_min: " + str(r_min) + " min_len: " + str(min_len)) 
                # move the left pointer
                freq_s[s[l]] -= 1
                if freq_s[s[l]] == 0:
                    del freq_s[s[l]]
                if freq_s[s[l]] < freq_t[s[l]]: # if the count of that character in freq_s < count of that character in freq_t, then that character in t is not fully covered
                    curr_valid_chars -= 1
                l += 1
                #print("2 " + " l: " + str(l) + " r: " + str(r) + " window: "+ str(s[l:(r+1)]) + " curr_valid: " + str(curr_valid_chars))
                while l < r and s[l] not in freq_t:
                    freq_s[s[l]] -= 1
                    if freq_s[s[l]] == 0:
                        del freq_s[s[l]]
                    l += 1
                    #print("3 " + " l: " + str(l) + " r: " + str(r) + " window: "+ str(s[l:(r+1)]) + " curr_valid: " + str(curr_valid_chars))
        if r_min == -1 or l_min == -1:
            return ""
        else:
            return s[l_min:(r_min + 1)]

