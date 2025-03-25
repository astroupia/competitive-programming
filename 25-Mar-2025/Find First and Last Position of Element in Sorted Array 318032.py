# Problem: Find First and Last Position of Element in Sorted Array - https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left, right =  0, len(nums) - 1
        res = []

        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                while mid > 0 and nums[mid - 1] == target:
                    mid -= 1
                res.append(mid)
                mid = (left + right) // 2
                while mid < len(nums) - 1 and nums[mid + 1] == target:
                    mid += 1
                res.append(mid)
                return res
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
            
        return [-1, -1]

       