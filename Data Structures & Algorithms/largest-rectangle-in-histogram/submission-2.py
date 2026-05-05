class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)
        stack = []
        maxArea = 0

        for i in range(len(heights)):
            if not stack:
                stack.append(i)
                continue
                
            if heights[i] >= heights[stack[-1]]:
                stack.append(i)
                continue

            # en caso de que sea menor vamos a hacer un ciclo para eliminar menores
            while stack and heights[i] < heights[stack[-1]]:
                # calcular el area eliminada
                h =  heights[stack.pop()]
              
                maxArea = max(maxArea,((i - 1) - (stack[-1] if stack else -1)) * h)
            stack.append(i)
            
        return maxArea