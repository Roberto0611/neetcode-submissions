class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        numsMap = {}
        for num in nums:
            numsMap[num] = numsMap.get(num,0) + 1
            
            if numsMap[num] > 1:
                return num
            