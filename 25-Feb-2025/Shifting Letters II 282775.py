# Problem: Shifting Letters II - https://leetcode.com/problems/shifting-letters-ii/description/

class Solution:
    def shiftingLetters(self, s: str, shifts: List[List[int]]) -> str:
        n = len(s)
        diff = [0] * (n + 1)

        for start, end, direction in shifts:
            change = 1 if direction == 1 else -1
            diff[start] += change
            diff[end + 1] -= change

        shift_value = 0
        result = []
    
        for i in range(n):
            shift_value += diff[i]  
            new_char = chr((ord(s[i]) - ord('a') + shift_value) % 26 + ord('a'))
            result.append(new_char)

        return "".join(result)
