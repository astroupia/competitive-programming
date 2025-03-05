# Problem: Removing Stars From a String - https://leetcode.com/problems/removing-stars-from-a-string/

class Solution:
    def removeStars(self, s: str) -> str:
        stack = []

        for chr in s:
            if chr == "*":
                stack.pop()
            else:
                stack.append(chr)
        
        return "".join(stack)