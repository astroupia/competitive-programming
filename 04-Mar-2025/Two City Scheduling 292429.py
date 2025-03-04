# Problem: Two City Scheduling - https://leetcode.com/problems/two-city-scheduling/

class Solution:
    def twoCitySchedCost(self, costs: List[List[int]]) -> int:
        diff = []
        _min_cost = 0

        for ca, cb in costs:
            diff.append([cb - ca, ca, cb])\
        
        diff.sort()
        for i in range(len(diff)):
            if i < len(diff) // 2:
                _min_cost += diff[i][2]
            else:
                _min_cost += diff[i][1]
        
        return _min_cost