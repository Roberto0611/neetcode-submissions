class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0 
        r = len(height) - 1
        maxL = 0
        maxR = 0
        water = 0
        while l < r:
            # caimos en un hoyo?
            if maxL > height[l]:
                water += min(maxR,maxL) - height[l]
            if maxR > height[r]:
                water += min(maxR,maxL) - height[r]

            # actualizar maximos
            maxL = max(height[l], maxL)
            maxR = max(height[r], maxR)

            # mover punteros
            if height[l] < height[r]:
                l+=1
                continue
            r-=1
        return water
