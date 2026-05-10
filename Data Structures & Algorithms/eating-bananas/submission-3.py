class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        start = 1
        middle = 0
        k = -1

        end = max(piles)

        while start <= end:
            middle = (start + end) // 2
            kk = middle
            #print(f'start {start}, end {end}, middle {middle}')

            # eat bananas
            hh = 0
            for i in piles:
                hh += (i + kk - 1)//kk
        
            if hh > h:
                start = middle + 1
            else:
                if kk < k or k == -1:
                    k = kk
                end = middle - 1
        return k 
