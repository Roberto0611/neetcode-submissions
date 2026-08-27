class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        products = [1]
        inverse = [1]
        output = []
        n = len(nums)
        l = 0
        r = n - 1

        # calcular productos
        for i in nums:
            products.append(products[-1] * i)
        
        # calcular producto inverso
        for i in range(n-1,-1,-1):
            inverse.append(inverse[-1] * nums[i])
        
        # calcular el output
        for i in range(n):
            output.append(products[l] * inverse[r])
            l += 1
            r -= 1

        return output