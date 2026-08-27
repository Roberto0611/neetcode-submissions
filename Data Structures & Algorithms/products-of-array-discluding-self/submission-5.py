class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * (n)
        prefix = 1
        postfix = 1

        # calcular productos de izq. a der. y ponerlos en el output
        for i in range(n):
            output[i] = prefix
            prefix *= nums[i]

        # calcular producto inverso acumulado y multiplicarlo al output
        for i in range(n-1,-1,-1):
            output[i] *= postfix
            postfix *= nums[i]

        return output