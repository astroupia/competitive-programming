# Problem: Search a 2D Matrix - https://leetcode.com/problems/search-a-2d-matrix/

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = -1
        i = 0
        low, high = 0, len(matrix) - 1
        while low <= high:
            mid = (low + high) // 2
        
            if matrix[mid][0] <= target <= matrix[mid][len(matrix[0]) - 1]:
                row = mid
                break
            elif matrix[mid][0] < target:
                low = mid + 1
            else:
                high = mid - 1
            
        if row == -1:
            return False

        left, right = 0, len(matrix[0]) - 1
        while left <= right:
            mid = (left + right) // 2
            if matrix[row][mid] == target:
                return True

            if matrix[row][mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False 
