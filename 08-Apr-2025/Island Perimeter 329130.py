# Problem: Island Perimeter - https://leetcode.com/problems/island-perimeter/description/

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        visited = [[False for i in range(len(grid[0]))] for i in range(len(grid))]
        
        def inbound(row, col):
            nonlocal grid
            if -1 < row < len(grid) and -1 < col < len(grid[0]):
                return True
            return False  
            
        parmeter = 0
        def dfs(visited, row, col):
            nonlocal directions
            nonlocal grid
            nonlocal parmeter
            
            visited[row][col] = True
            
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                if inbound(new_row, new_col) and grid[new_row][new_col]:
                    if not visited[new_row][new_col]:
                        dfs(visited, new_row, new_col)
                else:
                    parmeter += 1
        
        for m in range(len(grid)):
            for n in range(len(grid[0])):
                if grid[m][n] == 1:
                    dfs(visited, m, n) 
                    return parmeter
        
        return 0