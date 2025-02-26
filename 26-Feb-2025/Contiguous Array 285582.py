# Problem: Contiguous Array - https://leetcode.com/problems/contiguous-array/

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        _max = 0
        count_dict = defaultdict(int)
        count_dict[0] = -1
        running_sum = 0

        for i, num in enumerate(nums):
            running_sum += num if num == 1 else -1

            if running_sum in count_dict:
                _max = max(_max, i - count_dict[running_sum])
            
            else:
                count_dict[running_sum] = i
        
        return _max