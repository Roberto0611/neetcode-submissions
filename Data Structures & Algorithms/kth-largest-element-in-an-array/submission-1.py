''' 
Para este approach lo que hacemos es convertir la lista original a valores negativos, para hacer un max heap, despues simplemente hacemos pop de los primeros k elementos y devolvemos el ultimo cambiando su signo para que quede como originalmente estaba en la lista. 
'''

import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # convert to negative
        for i in range(len(nums)):
            nums[i] = -nums[i]
        
        # make a heap
        heapq.heapify(nums)

        # pop
        for i in range(k):
            n = heapq.heappop(nums)

        return -n 