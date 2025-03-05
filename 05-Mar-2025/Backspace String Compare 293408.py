# Problem: Backspace String Compare - https://leetcode.com/problems/backspace-string-compare/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        stack1 = []
        stack2 = []

        for chr in s:
            if chr == "#":
                if stack1:
                    stack1.pop()
            else:
                stack1.append(chr)
        
        for chr in t:
            if chr == "#":
                if stack2:
                    stack2.pop()
            else:
                stack2.append(chr)
        
        return stack1 == stack2
        