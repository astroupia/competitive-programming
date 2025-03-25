# Problem: Capacity To Ship Packages Within D Days - https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/

class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        def check(value):
            nonlocal days
            total, ships = 0, 1
            for weight in weights:
                if total + weight > value:
                    ships += 1
                    total = 0
                total += weight
            return ships <= days

        left, right = max(weights), sum(weights)
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right = mid
            else:
                left = mid + 1  
        return right 
        