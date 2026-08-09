class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # repaso 8 de Agosto 2026

        # lo primero que haremos es hacer un binary search sobre las columnas para saber en cual esta el target
        left = 0
        rigth = len(matrix) - 1
        m = -1
        
        while left <= rigth:
            mid = left + (rigth - left) // 2

            if matrix[mid][0] == target:
                return True

            if matrix[mid][0] > target:
                rigth = mid - 1

            if matrix[mid][0] < target:
                if matrix[mid][-1] > target:
                    m = mid
                    break
                if matrix[mid][-1] == target:
                    return True
                else:
                    left = mid + 1
        
        if m == -1:
            print('false primero')
            return False
        # lo segundo que hacemos es la busqueda binaria clasica en ese array
        left = 0
        rigth = len(matrix[m]) - 1

        while left <= rigth:
            mid = left + (rigth - left) // 2
            print(mid)

            if matrix[m][mid] == target:
                return True
            
            if matrix[m][mid] > target:
                rigth = mid - 1
            
            if matrix[m][mid] < target:
                left = mid + 1

        return False