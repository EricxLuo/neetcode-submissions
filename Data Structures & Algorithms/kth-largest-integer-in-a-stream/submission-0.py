class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.arr = nums
        heapq.heapify(self.arr)
        self.k = k
        while len(self.arr) > self.k:
            heapq.heappop(self.arr)

    

    def add(self, val: int) -> int:
        heapq.heappush(self.arr, val)
        if len(self.arr) > self.k:
            heapq.heappop(self.arr)
        return self.arr[0]
        
        
    
        
        