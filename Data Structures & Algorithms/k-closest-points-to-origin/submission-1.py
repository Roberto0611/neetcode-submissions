'''
Aqui la estrategia que seguimos es usar un array de dos dimensiones para guardar los datos en un heap, acomodarlos en base a la posicion 0 que equivale a la distancia pero armar la lista final en base al elementos 2 osea la distancia 
'''

import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        distanceHeap = []
        
        # loop sobre los puntos
        for point in points:
            distance = math.sqrt((0 - point[0])**2 + (0 - point[1])**2)

            distanceHeap.append([distance,point])
            
        heapq.heapify(distanceHeap)

        for i in range(k):
            result.append(heapq.heappop(distanceHeap)[1])
        
        return result
            