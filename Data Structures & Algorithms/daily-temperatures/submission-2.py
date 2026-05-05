class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures)
        
        for index,temperature in enumerate(temperatures):
            while stack and temperature > temperatures[stack[-1]]:
                res[stack[-1]] = index - stack[-1]
                stack.pop()
            stack.append(index)
        return res