class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        output = []
        nums.sort()
        # num es el puntero i
        for index,num in enumerate(nums):
            if index != 0 and num == nums[index-1]:
                continue
            target = num * -1

            # ahora nos queda two sum II
            j = index + 1
            k = len(nums) - 1 
            while j < k:
                if target == nums[j] + nums[k]:
                    output.append([nums[j],nums[k],num])
                    k-=1
                    j+=1
                    # evitar duplicados
                    while j < k:
                        if nums[k] == nums[k+1]:
                            k-=1
                            continue
                        if nums[j] ==  nums[j-1]:
                            j+=1
                            continue
                        break
                    continue
                if target < nums[j] + nums[k]:
                    k-=1 
                    continue
                else:
                    j+=1
        return output
