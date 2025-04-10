# Problem: Number of Provinces - https://leetcode.com/problems/number-of-provinces/

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        BLACK, GRAY, WHITE = 2, 1, 0
        graph = defaultdict(list)
        m, n = len(isConnected), len(isConnected[0])
        for row in range(m):
            for col in range(n):
                if isConnected[row][col]:
                    graph[row].append(col)
        
        color = [WHITE for i in range(len(graph))]
        def dfs(node):
        
            color[node] = GRAY 
            for extra in graph[node]:
                if color[extra] == WHITE:
                    dfs(extra)
           
        provinces = 0
        for node in range(len(graph)):
            if color[node] == WHITE:
                dfs(node)
                provinces += 1
            
        return provinces 


        
