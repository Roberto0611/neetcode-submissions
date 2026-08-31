import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        # we make a max heap
        # first we convert all to negative
        for i in range(len(stones)):
            stones[i] = -stones[i]
        
        # make the heap
        heapq.heapify(stones)

        # main loop
        while len(stones) >= 2:
            # we take the 2 max stones
            x = -heapq.heappop(stones)
            y = -heapq.heappop(stones)

            # we smash the stones
            if x == y:
                continue
            
            y = y - x

            # we add the new stone
            heapq.heappush(stones,y)
        
        if len(stones) == 0:
            return 0
            
        return -stones[0]