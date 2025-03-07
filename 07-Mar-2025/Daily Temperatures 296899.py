# Problem: Daily Temperatures - https://leetcode.com/problems/daily-temperatures/

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0] * len(temperatures) 

        for i, num in enumerate(temperatures):
            while stack and stack[-1][0] < num:
                diff = i - stack[-1][1]
                res[stack[-1][1]] = diff
                stack.pop()

            stack.append((num, i))
        
        return res