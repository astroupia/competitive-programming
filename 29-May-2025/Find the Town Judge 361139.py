# Problem: Find the Town Judge - https://leetcode.com/problems/find-the-town-judge/

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        score = [0] * (n + 1)  # 1-based indexing

        for a, b in trust:
            score[a] -= 1  # a trusts someone
            score[b] += 1  # b is trusted
    
        for i in range(1, n + 1):
            if score[i] == n - 1:
                return i
    
        return -1