# Problem: Couse Schedule - https://leetcode.com/problems/course-schedule/

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        WHITE, GRAY, BLACK = 0, 1, 2
        color = [WHITE for i in range(numCourses)]
        no_cycle = True
        graph = [[] for i in range(numCourses)]

        def dfs(node):
            flag = True    
            color[node] = GRAY
            
            for neig in graph[node]:
                if color[neig] == WHITE:
                    flag = flag and dfs(neig)
                elif color[neig] == GRAY:
                    return False
                    
            color[node] = BLACK 
            return flag
        
        for end, strt in prerequisites:
            graph[strt].append(end)
        
        for node in range(numCourses):
            if color[node] == WHITE:
                no_cycle = no_cycle and dfs(node)
            
        return no_cycle 
            

