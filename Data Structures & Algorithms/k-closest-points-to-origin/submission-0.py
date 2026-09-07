import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        distanceHeap = []
        heapq.heapify(distanceHeap)
        
        # loop sobre los puntos
        for point in points:
            distance = math.sqrt((0 - point[0])**2 + (0 - point[1])**2)
            distPos = [distance,point]
            
            heapq.heappush(distanceHeap,distPos)

        for i in range(k):
            result.append(heapq.heappop(distanceHeap)[1])
        
        return result
            