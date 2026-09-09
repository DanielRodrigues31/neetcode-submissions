class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        
        # if string is empty, immediately return 0
        if len(s) == 0:
            return maxLen
        
        # iterate r through string
        for r in range(len(s)):
            
            # shrink window, if r is in current window (without r)
            while s[r] in s[l:r]:
                l += 1
            # set maxLen to highest of currentwindow or maxLen
            maxLen = max(maxLen, (r - l) + 1)
            
        # return result
        return maxLen

                

        