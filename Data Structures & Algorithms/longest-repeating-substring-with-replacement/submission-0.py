class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        l = 0
        longest = 0
        freq = 0
        maxDict = {}
        for r in range(len(s)):
            maxDict[s[r]] = maxDict.get(s[r],0) + 1
            freq = max(maxDict.values())
            while (r - l + 1) - freq >  k:
                maxDict[s[l]] -=1
                l+=1
            
            longest = max(longest, r-l+1)
    
        return longest

        

