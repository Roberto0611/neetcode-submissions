class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # ordenar la lista
        nums.sort()

        # repasar uno por uno 
        nextNum = 0
        count = 1
        maxCount = 0

        for i,num in enumerate(nums):
            if i == len(nums) - 1:
                if(count > maxCount):
                    maxCount = count
                break

            nextNum = nums[i + 1]
            if nextNum == num:
                continue
            if nextNum == num + 1:
                count += 1
            else:
                if(count > maxCount):
                    maxCount = count
                count = 1

        return maxCount