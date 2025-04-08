# Problem: Find if Path Exists in Graph - https://leetcode.com/problems/find-if-path-exists-in-graph/

class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        graph = defaultdict(list)
        for strt, dest in edges:
            graph[strt].append(dest)
            graph[dest].append(strt)
    
        visited = defaultdict(list)
        return self.dfs(source, set(), destination, graph)

    def dfs(self, node, visited, dest, graph) -> bool:
        if node == dest:
            return True
        visited.add(node)

        for neigh in graph[node]:
            if neigh not in visited:
                res = self.dfs(neigh, visited, dest, graph)
                if res == True:
                    return True
        return False  