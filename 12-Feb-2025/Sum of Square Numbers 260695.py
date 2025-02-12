# Problem: Sum of Square Numbers - https://leetcode.com/problems/sum-of-square-numbers/

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left, right = 0, int(c ** 0.5)

        while left <= right:
            if left ** 2 + right ** 2 > c:
                right -= 1
            elif left ** 2 + right ** 2 < c:
                left += 1
            else:
                return True

        return False