class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * (n)
        prefix = 1
        postfix = 1

        # calcular productos de izq. a der. y ponerlos en el output
        for i in range(n):
            output[i] = prefix # agregamos el prefix
            prefix *= nums[i] # aumentamos prefix

        # calcular producto inverso acumulado y multiplicarlo al output
        for i in range(n-1,-1,-1):
            output[i] *= postfix # multiplicamos sobre los resultados que ya tenemos
            postfix *= nums[i] # aumentamos el postifx

        return output