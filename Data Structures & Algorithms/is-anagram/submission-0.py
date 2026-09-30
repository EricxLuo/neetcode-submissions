class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countS = {}
        countT = {}

        for i in range (len(s)):

            countS[s[i]] = 1 + countS.get(s[i], 0) #same as 1 + count[s[i]], but parameter has default
            countT[t[i]] = 1 + countT.get(t[i], 0)

        for letter in countS:
            if countS[letter] != countT.get(letter,0):
                return False
        return True