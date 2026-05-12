class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums) - 1
        middle = 0
        output = 1001

        while start <= end:
            middle = (start + end)//2
            output = min(nums[start],nums[end],nums[middle],output)

            # move pointers
            if nums[middle] >= nums[end]:
                start = middle + 1
            else:
                end = middle - 1

        return output