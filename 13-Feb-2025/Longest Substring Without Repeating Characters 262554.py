# Problem: Longest Substring Without Repeating Characters - https://leetcode.com/problems/longest-substring-without-repeating-characters/

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, char_set = 0, set()
        length = 0

        for right in range(len(s)):
            if s[right] not in char_set:
                char_set.add(s[right])
            else:
                while s[right] in char_set:
                    char_set.discard(s[left])
                    left += 1
                char_set.add(s[right])
            length  = max(length, len(char_set))

        return length