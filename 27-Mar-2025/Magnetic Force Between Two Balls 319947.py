# Problem: Magnetic Force Between Two Balls - https://leetcode.com/problems/magnetic-force-between-two-balls/

class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        def check(value):
            ball = 1            
            last = position[0]
            for i in range(1, len(position)) :
                if last + value <= position[i]:
                    last = position[i]
                    ball += 1
                if ball >= m:
                    return True
            return ball >= m 

        left, right = 0, max(position)
        while right - left > 1:
            mid = (left + right) // 2
            if check(mid):
                left = mid
            else:
                right = mid
            
        return left 
