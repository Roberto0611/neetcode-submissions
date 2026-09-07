'''
Aqui la estrategia es diferente, hacemos un maxheap para limitarnos a k elementos y eliminamos la raiz cuadtrada por que realmente es inecesaria para conocer cual es el elemento mas cerca y asi ahorramos operaciones. Importante al final ya no sacamos con heappop por que eso ocupa log N por cada operacion, si no que simplemente recorremos el array 
'''

import math
import heapq

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        result = []
        distanceHeap = []
        
        # loop sobre los puntos
        for point in points:
            distance = (point[0])**2 + (point[1])**2

            if len(distanceHeap) >= k:
                heapq.heappushpop(distanceHeap,[-distance,point])
            else:
                heapq.heappush(distanceHeap,[-distance,point])
        
        for _, point in distanceHeap:
            result.append(point)
        
        return result
            