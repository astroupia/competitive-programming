# Problem: Minimum Height Trees - https://leetcode.com/problems/minimum-height-trees/

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        graph = defaultdict(set)
        for u, v in edges:
            graph[u].add(v)
            graph[v].add(u)
        
        que = deque([node for node in range(n) if len(graph[node]) == 1])
        nodes = n
        while nodes > 2:
            que_count = len(que)
            nodes -= que_count
            for _ in range(que_count):
                node = que.popleft()
                neighbor = graph[node].pop()
                graph[neighbor].remove(node)
                if len(graph[neighbor]) == 1:
                    que.append(neighbor)
        
        return list(que)