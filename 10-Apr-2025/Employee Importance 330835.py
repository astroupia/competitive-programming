# Problem: Employee Importance - https://leetcode.com/problems/employee-importance/

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        graph = defaultdict(list)
        importance = defaultdict(int)
        res = 0

        for value in employees:
            importance[value.id] = value.importance
            for node in value.subordinates:
                graph[value.id].append(node)

        def dfs(node):
            nonlocal res
            res += importance[node]
        
            if not graph[node]:
                return 

            for extra_node in graph[node]:
                dfs(extra_node) 

        dfs(id)
        return res
        
