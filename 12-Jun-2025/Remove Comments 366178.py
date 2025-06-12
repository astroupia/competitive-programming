# Problem: Remove Comments - https://leetcode.com/problems/remove-comments/

class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        blc = False
        curr = ""
        
        for l in source:
            if not blc:
                curr = ""
            i = 0
            while i < len(l):
                if blc:
                    if i + 1 < len(l) and l[i] == '*' and l[i + 1] == '/':
                        blc = False
                        i += 2
                    else:
                        i += 1
                else:
                    if i + 1 < len(l) and l[i] == '/' and l[i + 1] == '*':
                        blc = True
                        i += 2
                    elif i + 1 < len(l) and l[i] == '/' and l[i + 1] == '/':
                        break
                    else:
                        curr += l[i]
                        i += 1
            if not blc and curr:
                res.append(curr)
        
        return res