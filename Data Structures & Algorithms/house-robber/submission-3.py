class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        prev2, prev1 = nums[0],max(nums[0],nums[1])
        res = 0     
        for i in range(2,len(nums)):
            res = max(prev1, prev2 + nums[i])
            prev2 = prev1
            prev1 = res
        return prev1
