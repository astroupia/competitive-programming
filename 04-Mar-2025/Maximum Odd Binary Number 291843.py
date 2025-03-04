# Problem: Maximum Odd Binary Number - https://leetcode.com/problems/maximum-odd-binary-number/

class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        nums = sorted(s, reverse = True)

        for i in range(len(nums)):
            if nums[i] == "0":
                nums[i-1], nums[-1] = nums[-1], nums[i-1]
                break
        return "".join(nums)

