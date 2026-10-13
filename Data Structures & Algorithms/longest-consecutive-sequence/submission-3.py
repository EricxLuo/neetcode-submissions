class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        numSet = set(nums)
        res = 0
        for num in numSet:
            if num - 1 not in numSet:
                count = 1
                while (num + count) in numSet:
                    count +=1
                res = max(count,res)
        return res
        