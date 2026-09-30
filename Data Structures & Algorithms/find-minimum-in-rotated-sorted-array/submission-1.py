class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r = 0, len(nums) - 1

        small = nums[0]
        while l <= r:
            print(min(small,nums[l]))
            if nums[l] < nums[r]:
                return min(small,nums[l])
            
            mid = (l + r) // 2
            small = min(small,nums[mid])
            
            if nums[mid] >= nums[l]:
                l = mid + 1
            else:
                r = mid - 1
        return small

