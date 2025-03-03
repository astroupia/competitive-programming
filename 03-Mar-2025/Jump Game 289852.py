# Problem: Jump Game - https://leetcode.com/problems/jump-game/

class Solution:
    def canJump(self, nums: List[int]) -> bool: 
        if nums[0] == 0 and len(nums) == 1:
            return True

        if nums[0] == 0:
            return False

        right = len(nums) - 1
        jump = len(nums) - 2
        _FLAG = True 

        while right > -1 and jump > -1:
            if jump + nums[jump] >= right:
                jump -= 1
                right = jump + 1
                _FLAG = True
            else:
                jump -= 1
                _FLAG = False
        
        return _FLAG

