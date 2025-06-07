# Problem: Print Words Vertically - https://leetcode.com/problems/print-words-vertically/description/

class Solution:
    def printVertically(self, s: str) -> List[str]:
        words = s.split()
        max_len = max(len(word) for word in words)
        result = []

        for i in range(max_len):
            vertical = ''
            for word in words:
                if i < len(word):
                    vertical += word[i]
                else:
                    vertical += ' '
            result.append(vertical.rstrip())  # remove trailing spaces

        return result