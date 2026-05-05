class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        stack = []
        pair.sort(reverse=True)

        for p,s in pair:
            if len(stack) == 0 or (target - p)/s > stack[-1]:
                stack.append((target - p)/s)
            
        return len(stack)
