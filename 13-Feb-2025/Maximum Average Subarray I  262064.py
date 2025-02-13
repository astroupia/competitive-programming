# Problem: Maximum Average Subarray I  - https://leetcode.com/problems/maximum-average-subarray-i/

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        left, right = 0, k-1
        window = sum(nums[left: right + 1])
        summation = window 
        
        while right < len(nums) - 1:
            right += 1
            window = (window - nums[left]) + nums[right]
            summation = max(summation, window)
            left += 1
            
        average_value = summation / k

        return average_value   
