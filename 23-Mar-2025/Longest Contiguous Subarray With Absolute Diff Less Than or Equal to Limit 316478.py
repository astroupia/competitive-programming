# Problem: Longest Contiguous Subarray With Absolute Diff Less Than or Equal to Limit - https://leetcode.com/problems/longest-continuous-subarray-with-absolute-diff-less-than-or-equal-to-limit/

class Solution:
    def longestSubarray(self, nums: list[int], limit: int) -> int:
        min_d = deque()
        max_d = deque()
        l = 0
        ans = 0
        for r, num in enumerate(nums):
            while min_d and num < min_d[-1]:
                min_d.pop()
            min_d.append(num)
            while max_d and num > max_d[-1]:
                max_d.pop()
            max_d.append(num)
            while max_d[0] - min_d[0] > limit:
                if nums[l] == min_d[0]:
                    min_d.popleft()
                if nums[l] == max_d[0]:
                    max_d.popleft()
                l += 1
            ans = max(ans, r - l + 1)
        return ans
