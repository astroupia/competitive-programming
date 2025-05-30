# Problem: Minimum Time to Repair Cars - https://leetcode.com/problems/minimum-time-to-repair-cars/

class Solution:
    def repairCars(self, ranks: List[int], cars: int) -> int:
        def bs(time):
            repaired = 0
            for r in ranks:
                repaired += int(math.isqrt(time // r))
                if repaired >= cars:
                    return True
            return False

        low, high = 1, min(ranks) * cars * cars
        ans = high
    
        while low <= high:
            mid = (low + high) // 2
            if bs(mid):
                ans = mid
                high = mid - 1
            else:
                low = mid + 1
    
        return ans