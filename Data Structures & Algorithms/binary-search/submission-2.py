class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0
        end = len(nums) - 1

        while(start <= end):
            # get middle
            middle = (start + end)//2
            
            if target == nums[middle]:
                return middle
            
            if target > nums[middle]:
                start = middle + 1
            
            if target < nums[middle]:
                end = middle - 1
            
        return -1