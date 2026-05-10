class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        index = -1
        n = len(matrix)
        start = 0
        end = len(matrix[0]) - 1
        middle = 0

        for i in range(n):
            if matrix[i][-1] > target:
                index = i
                break
            if matrix[i][-1] == target:
                return True
        
        # not found
        if index == -1:
            return False
        
        # found then binary search on that matrix
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
