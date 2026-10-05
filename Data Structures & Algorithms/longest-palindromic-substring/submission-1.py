class Solution:
    def longestPalindrome(self, s: str) -> str:

        start = 0
        end = 0
        largest = 0
        for i in range(len(s)):
            l,r = i,i# odd
           
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r-l+1 >= largest:
                    start = l
                    end = r
                    largest = r-l+1
                l -=1
                r +=1

            l,r = i,i+1   #even
            while l >= 0 and r < len(s) and s[l] == s[r]:       
                if r-l+1 >= largest:
                    start = l
                    end = r
                    largest = r-l+1         
                l -=1
                r +=1     
         
        return s[start:end + 1]

        