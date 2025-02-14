# Problem: Max Consecutive Ones III - https://leetcode.com/problems/max-consecutive-ones-iii/

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left, count, min_value = 0, 0, float("-inf")

        if sum(nums) == 0:
            return k

        for right in range(len(nums)):
            if nums[right] == 1:
                count += 1
    
            while left < right and count + k < right - left + 1:
                if nums[left] == 1:
                    count -= 1
                left += 1    
            min_value = max(min_value, right - left + 1)

        return min_value