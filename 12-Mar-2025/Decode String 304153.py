# Problem: Decode String - https://leetcode.com/problems/decode-string/

class Solution: 
    def decodeString(self, s: str) -> str:
        close = [i for i in range(len(s))]
        stack = []

        for ind, char in enumerate(s): 
            if char == '[':
                stack.append(ind)
            elif char == ']':
                close[stack[-1]] = ind
                stack.pop()
        print(close)
        def decode(i, j):
            nonlocal s
            nonlocal close
            num = ''
            ans = ''
            
            k = i
            while k < j:
                if s[k].isalpha():
                    ans += s[k]
                elif s[k].isdigit():
                    num += s[k]
                else:
                    print(num, k , i , j)
                    ans += int(num) * decode(k + 1, close[k])
                    num = ''
                    k = close[k]
                
                k += 1
                
            return ans  
        return decode(0, len(s))
