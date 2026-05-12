class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        middle = 0
        output = 1001

        # first we search our start point
        while nums[start] > nums[end]:
            start+=1
        
        while start <= end:
            middle = (start + end) // 2

            output = min(nums[start],nums[end],nums[middle],output)

            start = middle + 1;            

        return output