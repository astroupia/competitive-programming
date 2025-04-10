# Problem: Max Area of Island - https://leetcode.com/problems/max-area-of-island/

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        m, n = len(grid), len(grid[0])
        visited = [[0 for j in range(n)] for i in range(m)]
        _max = 0

        def inbound(row, col):
            return 0 <= row < m and 0 <= col < n

        area = 0
        def dfs(row, col):
            nonlocal area 
            area += 1

            visited[row][col] = 1
            for dx, dy in directions:
                new_row = row + dx
                new_col = col + dy

                if inbound(new_row, new_col) and not visited[new_row][new_col]:
                    if grid[new_row][new_col]:
                        dfs(new_row, new_col)                 
            
            return area

        for row in range(m):
            for col in range(n):
                if not visited[row][col] and grid[row][col]:
                    _max = max(_max, dfs(row, col))
                    area = 0

        return _max