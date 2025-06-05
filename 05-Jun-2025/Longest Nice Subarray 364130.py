# Problem: Longest Nice Subarray - https://leetcode.com/problems/longest-nice-subarray/

class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        max_len = 0
        left = 0
        bitmask = 0

        for right in range(len(nums)):
            # If nums[right] shares bits with bitmask, shrink window
            while (bitmask & nums[right]) != 0:
                bitmask ^= nums[left]  # Remove nums[left] from bitmask
                left += 1
            
            bitmask |= nums[right]  # Add nums[right] to bitmask
            max_len = max(max_len, right - left + 1)

        return max_len
