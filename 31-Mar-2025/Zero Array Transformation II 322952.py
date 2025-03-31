# Problem: Zero Array Transformation II - https://leetcode.com/problems/zero-array-transformation-ii/

class Solution:
    def minZeroArray(self, nums: List[int], queries: List[List[int]]) -> int:
        n = len(nums)
        m = len(queries)
        
        def check(k: int) -> bool:
            diff = [0] * (n + 1)
            for i in range(k):
                l, r, v = queries[i]
                diff[l] += v
                if r + 1 < n:
                    diff[r + 1] -= v
            cur = 0
            for i in range(n):
                cur += diff[i]
                if cur < nums[i]:
                    return False
            return True
            
        lo, hi = 0, m + 1
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                hi = mid
            else:
                lo = mid + 1
        return lo if lo <= m else -1
