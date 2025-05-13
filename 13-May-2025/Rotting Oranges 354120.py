# Problem: Rotting Oranges - https://leetcode.com/problems/rotting-oranges/

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        q = deque()
        fresh, time = 0, 0
        row, col = len(grid), len(grid[0])
        
        def inbound(r, c):
            return 0 <= r < row and 0 <= c < col

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 1:
                    fresh += 1
                if grid[r][c] == 2:
                    q.append([r, c])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while q and fresh > 0:
            
            for i in range(len(q)):
                r, c = q.popleft()
                for dr, dc in directions:
                    rr, cc = r + dr, c + dc

                    if not inbound(rr, cc) or grid[rr][cc] != 1:
                        continue 
                    grid[rr][cc] = 2
                    fresh -= 1 
                    q.append([rr, cc])
            time += 1
        return time if fresh == 0 else -1
                    