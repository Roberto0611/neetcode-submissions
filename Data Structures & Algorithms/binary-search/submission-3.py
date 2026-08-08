class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # repaso 8 de Agosto 2026
        left = 0
        rigth = len(nums) - 1

        while left <= rigth:
            # buscar el de en medio
            mid = left + (rigth - left) // 2

            if nums[mid] == target:
                return mid

            if nums[mid] > target:
                rigth = mid - 1
                continue
    
            if nums[mid] < target:
                left = mid + 1
                continue
        return -1