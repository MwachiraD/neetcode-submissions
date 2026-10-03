import heapq
class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            x = heapq.heappop(heap)
            y = heapq.heappop(heap)

            if x != y:
                heapq.heappush(heap , x - y)

        if heap:
            return abs(heap[0]) 
        else:
            return 0

        
            
        