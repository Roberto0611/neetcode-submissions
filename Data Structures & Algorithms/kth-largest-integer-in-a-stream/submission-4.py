"""

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
        print(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) >= self.k:
            heapq.heappushpop(self.nums,val)
        else:
            heapq.heappush(self.nums,val)
        n = self.nums[0]
        return n
        