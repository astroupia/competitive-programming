# Problem: Minimum Number of Arrows to Burst Balloons - https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        if not points:
            return 0

        points.sort(key=lambda interval: interval[1])
        arrows = 0
        curr = None
        for start, end in points:
            if curr is None or start > curr:
                arrows += 1
                curr = end

        return arrows
