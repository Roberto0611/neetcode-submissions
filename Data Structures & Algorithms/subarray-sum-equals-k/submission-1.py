class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        actualSum = 0
        history = {}
        history[0] = 1

        for i in nums:
            actualSum += i

            if (actualSum - k) in history:
                count += history[actualSum - k]
            
            n = history.get(actualSum,0)
            history[actualSum] = n + 1 
        return count
