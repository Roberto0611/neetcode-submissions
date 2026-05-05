class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        rigthP = []
        leftP = []
        output = []

        for i in range(len(nums)):
            rigthProduct = 1
            leftProduct = 1

            if i == 0:
                leftP = []
                rigthP = nums[i+1:]
                print(leftP)
                print(rigthP)
            elif i == len(nums):
                rigthP = []
                leftP = nums[:i]
                print(leftP)
                print(rigthP)
            else:
                rigthP = nums[i+1:]
                leftP = nums[:i]
                print(leftP)
                print(rigthP)

            # rigth
            if rigthP != []:
                for num in rigthP:
                    rigthProduct = rigthProduct * num

            # left
            if leftP != []:
                for num in leftP:
                    leftProduct = leftProduct * num

            output.append(leftProduct * rigthProduct)
        return output