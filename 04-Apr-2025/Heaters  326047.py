# Problem: Heaters  - https://leetcode.com/problems/heaters/

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        N = len(heaters)
        heaters.extend([float("-inf"), float("inf")])
        houses.sort()
        heaters.sort()

        def check(value):
            for house in houses:
                index = bisect.bisect_left(heaters, house)
                if min(abs(heaters[index] - house), abs(house - heaters[index - 1] )) > value:
                    return False
            return True

        left, right = 0, 2 ** 100
        while left < right:
            mid = (left + right) // 2
            if check(mid):
                right =  mid 
            else:
                left = mid + 1
            
        return left 

 