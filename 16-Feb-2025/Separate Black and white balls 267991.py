# Problem: Separate Black and white balls - https://leetcode.com/problems/separate-black-and-white-balls/

class Solution:
    def minimumSteps(self, s: str) -> int:
        
        ones = [i for i, char in enumerate(s) if char == '1']
        k = len(ones)
        if k == 0:
            return 0

        n = len(s)
        total = 0
        for i in range(k):
            target = (n - k) + i
            total += target - ones[i]
        return total