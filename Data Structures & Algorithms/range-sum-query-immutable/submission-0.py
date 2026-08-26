class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixSum = [0] # we start with 0 for edgecases
        actualSum = 0
        
        # save the prefix sums list
        for i in nums:
            actualSum += i
            self.prefixSum.append(actualSum)        

    def sumRange(self, left: int, right: int) -> int:
        # search the two indexs
        result = self.prefixSum[right + 1] - self.prefixSum[left]
        return result 


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)