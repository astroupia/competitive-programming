# Problem: Product of Array Except Self - https://leetcode.com/problems/product-of-array-except-self/

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix_product = [1] * len(nums) 
        postfix_product = [1] * len(nums)
        result = []

        for i in range(1, len(nums)):
            prefix_product[i] = nums[i - 1] * prefix_product[i - 1]
   
        for i in range(len(nums) - 2, -1, -1):
            postfix_product[i] = nums[i + 1] * postfix_product[i + 1]
       
        for i in range(len(nums)):
            result.append(postfix_product[i] * prefix_product[i])
            
        return result