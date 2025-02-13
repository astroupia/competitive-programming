# Problem: Permutation in String - https://leetcode.com/problems/permutation-in-string/

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s = Counter(s1)
        left = 0
        
        for right in range(len(s2)):
            count_s[s2[right]] -= 1
            if count_s[s2[right]] == 0:
                del count_s[s2[right]]
            
            while s2[right] in count_s and count_s[s2[right]] < 0:
                count_s[s2[left]] = count_s.get(s2[left], 0) + 1
                if count_s[s2[left]] == 0:
                    del count_s[s2[left]]
                left += 1
            if not count_s:
                return True
            
        return False