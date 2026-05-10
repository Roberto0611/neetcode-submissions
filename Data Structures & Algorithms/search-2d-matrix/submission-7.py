class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        start = 0
        end = len(matrix) - 1 
        middle = 0
        index = -1

        # 1st binary search
        while start <= end:
            middle = (start + end)//2

            if middle >= len(matrix):
                break

            if matrix[middle][-1] > target and matrix[middle][0] < target:
                index = middle
                break
            
            if matrix[middle][-1] > target and matrix[middle][0] > target:
                end = middle - 1
            
            if matrix[middle][-1] < target:
                start = middle + 1
                
            if  matrix[middle][-1] == target or  matrix[middle][0] == target:
                return True

        if index == -1:
            return False

        # 2nd binary search 
        start = 0
        end = len(matrix) - 1

        while start <= end:
            # get middle
            middle = (start + end) // 2

            if matrix[index][middle] == target:
                return True
            
            if matrix[index][middle] > target:
                end = middle - 1
            
            if matrix[index][middle] < target:
                start = middle + 1

        return False