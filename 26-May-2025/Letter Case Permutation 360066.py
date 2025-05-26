# Problem: Letter Case Permutation - https://leetcode.com/problems/letter-case-permutation/

class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        res = []

        def dfs(idx, path):
            if idx == len(s):
                res.append(path)
                return
            
            if s[idx].isalpha():
                dfs(idx + 1, path + s[idx].lower())
                dfs(idx + 1, path + s[idx].upper())
            else:
                dfs(idx + 1, path + s[idx])

        dfs(0, "")
        return res