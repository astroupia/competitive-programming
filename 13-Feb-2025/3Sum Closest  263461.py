# Problem: 3Sum Closest  - https://leetcode.com/problems/3sum-closest/

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        result = []

        for i in range(0, len(nums)):
            left, right = i+1, len(nums) - 1

            while left < right:
                summation = nums[i] + nums[left] + nums[right]
                diff = target - summation
                result.append((abs(diff), summation))

                if summation > target :
                    right -= 1
                else:   
                    left += 1

        result.sort()        
        return  result[0][1]
    
