class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def findMe(nums,target,start,end):
            print(f'ventana {nums[start:end+1]}')

            # no existe
            if start > end:
                return -1
            
            # sacar middle
            middle = round((start+end) / 2)

            # recursividad
            if target == nums[middle]:
                return middle
            
            if target > nums[middle]:
                return findMe(nums,target,middle+1,end)
            
            if target < nums[middle]:
                return findMe(nums,target,start,middle-1)


        return findMe(nums,target,0,len(nums)-1)