# Problem: Simplify Path - https://leetcode.com/problems/simplify-path/

class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        paths = path.split("/")

        for pth in paths:
            if pth == "." or pth == "":
                continue 
            elif pth == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(pth)
            
        return "/" + "/".join(stack)