"""
Cambiamos el enfoque en este segundo intento, mantenemos un min heap pero limitandolo a k elementos
de esta manera siempre el que quede hasta arriba sera el mayor elemento k. 
"""

import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.nums = nums

        heapq.heapify(self.nums)

        # podamos la lista para dejarla en k elementos
        while len(self.nums) > self.k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) >= self.k:
            heapq.heappushpop(self.nums,val) # hacemos todo en una sola operacion
        else:
            heapq.heappush(self.nums,val)
        n = self.nums[0]
        return n
        