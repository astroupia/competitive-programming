# Problem: Find Eventual Safe States - https://leetcode.com/problems/find-eventual-safe-states/

class Solution:
    def eventualSafeNodes(self, graph):
        n = len(graph)
        reverse_graph = defaultdict(list)
        out_degree = [0] * n
        for u in range(n):
            for v in graph[u]:
                reverse_graph[v].append(u)
            out_degree[u] = len(graph[u])
        queue = deque([i for i in range(n) if out_degree[i] == 0])
        safe = [False] * n

        while queue:
            node = queue.popleft()
            safe[node] = True
            for prev in reverse_graph[node]:
                out_degree[prev] -= 1
                if out_degree[prev] == 0:
                    queue.append(prev)
        return [i for i, is_safe in enumerate(safe) if is_safe]
