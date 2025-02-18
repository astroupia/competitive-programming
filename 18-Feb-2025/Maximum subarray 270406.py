# Problem: Maximum subarray - https://leetcode.com/problems/maximum-subarray/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        total_max = float("-inf")
        running_sum = 0

        for num in nums:
            running_sum += num
            running_sum = max(num, running_sum)
            total_max = max(total_max, running_sum)

        return total_max