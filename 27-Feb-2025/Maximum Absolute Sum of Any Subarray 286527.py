# Problem: Maximum Absolute Sum of Any Subarray - https://leetcode.com/problems/maximum-absolute-sum-of-any-subarray/

class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        _min_prefix = nums[0]
        _max_prefix = nums[0]
        global_max = nums[0]
        global_min = nums[0]

        for num in nums[1:]:
            _min_prefix = min(num, num + _min_prefix)
            _max_prefix = max(num, num + _max_prefix)
            global_max = max(global_max, _max_prefix)
            global_min = min(global_min, _min_prefix)
        
        return max(global_max, -global_min)