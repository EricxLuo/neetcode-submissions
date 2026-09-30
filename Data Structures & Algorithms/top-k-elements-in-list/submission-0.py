class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = []     
        for num in nums:
            count[num] = 1 + count.get(num,0)
        
        for i in range(k):
            top = max(count,key=count.get)
            freq.append(top)
            count.pop(top)
            print(freq)
        return freq