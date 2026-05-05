class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        maxL = 0
        maxR = 0
        maxCompare = 0
        water = [0] * len(height)
        while l < r: 
            # saltar inecesarios
            if height[l] < maxL:
                l+=1 
                continue
            if height[r] < maxR:
                r-=1 
                continue

            # compare
            compare = min(height[l],height[r])
            if compare > maxCompare:
                # atrapar el agua
                # print('TRAP')
                for i in range(l+1,r):    
                    water[i] = max((compare - height[i]),water[i])          
                # print(water)
                # actualizar maxCompare
                maxCompare = compare

            # aumentar el puntero mas chico
            if height[l] < height[r]:
                l+=1 
                continue
            r-=1 
        # retornar la suma de agua
        return sum(water)