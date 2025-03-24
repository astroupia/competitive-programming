# Problem: The k-th Lexicographical String of All Happy Strings of Length n - https://leetcode.com/problems/the-k-th-lexicographical-string-of-all-happy-strings-of-length-n/description/

class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        self.count = 0
        self.result = ""
        
        def backtrack(s):
            nonlocal n
            if len(s) == n:
                self.count += 1
                if self.count == k:
                    self.result = s
                    return True 
                return False  
            
            for c in 'abc':
                if not s or s[-1] != c:
                    if backtrack(s + c):
                        return True 
            return False
        backtrack("")
        return self.result