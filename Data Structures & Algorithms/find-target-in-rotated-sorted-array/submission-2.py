class Solution:
    def search(self, nums: List[int], target: int) -> int:
        start = 0;
        end = len(nums) - 1;
        middle = 0;
        minNum = 1001;
        cut = 1001;

        # fist find the minimum
        while start <= end:
            middle = (end + start) // 2
            
            # find min index
            if minNum > nums[start]:
                minNum = nums[start]
                cut = start;
            
            if minNum > nums[end]:
                minNum = nums[end]
                cut = end
            
            if minNum > nums[middle]:
                minNum = nums[middle]
                cut = middle

            if nums[start] <= nums[middle]:
                start = middle + 1
            else:
                end = middle - 1

        # now we need to search in both lists

        # list 1
        start = 0;
        end = cut - 1;
        
        while start <= end:
            middle = (start + end) // 2;

            if nums[middle] == target:
                return middle;
            
            if nums[middle] >= target:
                end = middle - 1;
            else:
                start = middle + 1;

        # list 2
        start = cut;
        end = len(nums) - 1;
        
        while start <= end:
            middle = (start + end) // 2;

            if nums[middle] == target:
                return middle;
            
            if nums[middle] >= target:
                end = middle - 1;
            else:
                start = middle + 1;

        return -1;