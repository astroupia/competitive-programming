# Problem: Lexicographically Smallest Equivalent String - https://leetcode.com/problems/lexicographically-smallest-equivalent-string/

class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        strr = [i for i in range(26)]

        def find(x):
            if strr[x] != x:
                strr[x] = find(strr[x])
            return strr[x]

        def union(x, y):
            px = find(x)
            py = find(y)
            if px < py:
                strr[py] = px
            else:
                strr[px] = py

        for a, b in zip(s1, s2):
            union(ord(a) - ord('a'), ord(b) - ord('a'))
        res = []
        for c in baseStr:
            root = find(ord(c) - ord('a'))
            res.append(chr(root + ord('a')))

        return ''.join(res)