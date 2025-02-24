# Problem: Diagonal Traverse - https://leetcode.com/problems/diagonal-traverse/

class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        row = len(mat)
        col = len(mat[0])

        result = []
        current_row = current_col = 0
        upward_traversal = True

        while len(result) < row * col:
            result.append(mat[current_row][current_col])

            if upward_traversal:

                if current_col == col - 1:
                    current_row += 1
                    upward_traversal = False
                elif current_row == 0:
                    current_col += 1
                    upward_traversal = False
                else:
                    current_row -= 1
                    current_col += 1

            else:
                if current_row == row - 1:
                    current_col += 1
                    upward_traversal = True
                elif current_col == 0:
                    current_row += 1
                    upward_traversal = True
                else:
                    current_row += 1
                    current_col -= 1

        return result 

                    