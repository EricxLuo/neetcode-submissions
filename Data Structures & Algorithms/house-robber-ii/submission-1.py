class Solution:
    def rob(self, nums: List[int]) -> int:
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums[0],nums[1])
        def houseRob(house):

            prev2, prev1 = house[0], max(house[0],house[1])
            res = 0
            for i in range(2,len(house)):
                res = max(prev1, prev2 + house[i])
                prev2 = prev1
                prev1 = res
            return prev1

        return max(houseRob(nums[1:]), houseRob(nums[:-1]))
        
        