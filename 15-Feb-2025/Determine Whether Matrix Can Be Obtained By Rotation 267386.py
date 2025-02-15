# Problem: Determine Whether Matrix Can Be Obtained By Rotation - https://leetcode.com/problems/determine-whether-matrix-can-be-obtained-by-rotation/

class Solution:
    def findRotation(self, mat: List[List[int]], target: List[List[int]]) -> bool:
        n = len(mat)
        
        def rotate(mat: List[List[int]]) -> List[List[int]]:
            return [[mat[n - 1 - j][i] for j in range(n)] for i in range(n)]
        
        for _ in range(4):  
            if mat == target:
                return True
            mat = rotate(mat)  
        return False