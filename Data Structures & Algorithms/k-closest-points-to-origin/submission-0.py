class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap =[]
        mydict = defaultdict(list)
        heapq.heapify(heap)
        for coord in points:

            dist = math.sqrt((coord[0] - 0)**2 + (coord[1] - 0)**2)
            
            mydict[dist].append(coord)
            if len(heap) < k:
                heapq.heappush(heap, -dist)
            else:
                heapq.heappush(heap,-dist)
                heapq.heappop(heap)
            
        closest = []
      
        for distance in heap:
            point = mydict[-distance].pop()
            closest.append(point)
    
        return closest