# Problem: Letter Tile Possibilities - https://leetcode.com/problems/letter-tile-possibilities/description/

class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        freq = [0] * 26
        for c in tiles:
            freq[ord(c) - ord('A')] += 1
        count = 0
        def backtrack():
            nonlocal count
            for i in range(26):
                if freq[i] > 0:
                    freq[i] -= 1
                    count += 1
                    backtrack()
                    freq[i] += 1
        backtrack()
        return count