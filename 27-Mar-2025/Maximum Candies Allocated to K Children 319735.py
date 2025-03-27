# Problem: Maximum Candies Allocated to K Children - https://leetcode.com/problems/maximum-candies-allocated-to-k-children/

class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        if sum(candies) < k:
            return 0

        def check(value):
            total = 0
            for candy in candies:
                if candy >= value:
                    total += candy // value
            return total >= k
        
        left, right = 0, sum(candies) // k
        while left < right:
            mid = (left + right) // 2 + 1
            if check(mid):
                left = mid
            else:
                right = mid - 1
            
        return left