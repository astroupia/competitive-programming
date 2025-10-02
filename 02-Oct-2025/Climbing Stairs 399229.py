# Problem: Climbing Stairs - https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:
        one = 1
        two = 1

        for i in range (1, n):
            temp = one
            one = one + two 
            two = temp 
        
        return one