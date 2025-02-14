# Problem: Valid Palindrome II - https://leetcode.com/problems/valid-palindrome-ii/description/

class Solution:
    def validPalindrome(self, s: str) -> bool:
        left, count = 0, 0

        def is_valid(left, right):
            while left < right:
                if s[left] != s[right]:
                    return False
                left += 1
                right -= 1
            return True

        for right in range(len(s) - 1, len(s) // 2, -1):
            if s[left] == s[right]:
                left += 1
            elif s[left] != s[right]:
                if is_valid(left + 1, right):
                    return True
                elif is_valid(left, right - 1):
                    return True
                else:
                    return False
        
        return True
