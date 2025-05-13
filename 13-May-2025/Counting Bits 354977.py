# Problem: Counting Bits - https://leetcode.com/problems/counting-bits/

class Solution:
    def countBits(self, n: int) -> List[int]:
        ans = []
        for num in range(n + 1):
            ct = 0
            while num > 0:
                if num & 1 == 1:
                    ct += 1
                num >>= 1
            ans.append(ct)
        return ans