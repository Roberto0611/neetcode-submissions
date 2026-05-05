class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for index,temperature in enumerate(temperatures):
            while len(stack) > 0:
                if temperature > stack[-1][0]:
                    res[stack[-1][1]] = index - stack[-1][1]
                    stack.pop()
                    continue
                break
            stack.append([temperature,index])
        return res