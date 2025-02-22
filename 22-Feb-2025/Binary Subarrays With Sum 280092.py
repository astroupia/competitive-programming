# Problem: Binary Subarrays With Sum - https://leetcode.com/problems/binary-subarrays-with-sum/

class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        running_sum = 0 
        freq = defaultdict(int)
        count = 0 
        freq[0] = 1

        for num in nums:
            running_sum += num
            count += freq[running_sum - goal]

            freq[running_sum] += 1

        return count
    