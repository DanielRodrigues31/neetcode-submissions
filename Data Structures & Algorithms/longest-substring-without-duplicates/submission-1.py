class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLen = 0
        hashSet = {}
        
        # if string is empty, immediately return 0
        if len(s) == 0:
            return maxLen
        
        # iterate r through string
        for r in range(len(s)):

            # add char to hashmap
            hashSet[s[r]] = hashSet.get(s[r], 0) + 1
            
            # shrink window
            while hashSet.get(s[r], 0) > 1:

                # subtract count from char in hashmap
                hashSet[s[l]] = hashSet.get(s[l], 0) - 1

                # delete char from hashmap if 0 or less 
                if hashSet[s[l]] <= 0:
                    del(hashSet[s[l]])

                # increment l by 1 to shrink window
                l += 1

            # set maxLen to highest of currentwindow or maxLen
            maxLen = max(maxLen, (r - l) + 1)

        # return result
        return maxLen

                

        