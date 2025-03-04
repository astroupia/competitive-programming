# Problem: Split a String in Balanced Strings - https://leetcode.com/problems/split-a-string-in-balanced-strings/

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        right = 0
        r_count = l_count = 0
        res = 0

        while right < len(s):
            if s[right] == "R":
                r_count += 1
            else:
                l_count += 1
            
            if r_count == l_count:
                res += 1
                
            right += 1
        return res