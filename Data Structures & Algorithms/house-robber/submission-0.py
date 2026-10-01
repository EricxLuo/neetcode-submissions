class Solution:
    def rob(self, nums: List[int]) -> int:
        first, second = 0,0

        for num in nums:
            temp = max(num + first, second) #[first,second, num, num +  1, num + 2...]
            first = second
            second = temp
        return second