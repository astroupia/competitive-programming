# Problem: Combinations - https://leetcode.com/problems/combinations/

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []

        def backtrack(num, path):
            if len(path) == k:
                res.append(path[:])
                return 

            for candidate in range(num, n + 1):
                path.append(candidate)
                backtrack(candidate + 1, path)
                path.pop()
            
        backtrack(1, [])
        return res
