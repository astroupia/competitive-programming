# Problem: Minimum Window Substring - https://leetcode.com/problems/minimum-window-substring/submissions/

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        t_counter = Counter(t)
        left, count = 0, 0
        min_value = [float("-inf"), float("inf")]

        for right in range(len(s)):
            if s[right] in t_counter :
                t_counter[s[right]] -= 1
                if t_counter[s[right]] >= 0:
                    count += 1
            
            while count == len(t):
                if right - left < min_value[1] - min_value[0]:
                    min_value = [left, right] 
                if s[left] in t_counter:
                    t_counter[s[left]] += 1
                    if t_counter[s[left]] > 0:
                        count -= 1
                left += 1

        if min_value[0] == float("-inf"):
            return ""
        return s[min_value[0]: min_value[1]+1]
                 
            
        

