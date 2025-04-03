# Problem: Set Mismatch - https://leetcode.com/problems/set-mismatch/description/

class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        count_nums = Counter(nums)
        res = []
        for key, value in count_nums.items():
            if value > 1:
                res.append(key)
            
        nums_set = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in nums_set:
                res.append(i)
            
        return res 