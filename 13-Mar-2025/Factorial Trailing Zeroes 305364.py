# Problem: Factorial Trailing Zeroes - https://leetcode.com/problems/factorial-trailing-zeroes/

class Solution:
    def trailingZeroes(self, n: int) -> int:
        def count(n, power):
            if n < power:
                return 0
            
            return (n // power) + count(n, power * 5) 

        return count(n, 5)