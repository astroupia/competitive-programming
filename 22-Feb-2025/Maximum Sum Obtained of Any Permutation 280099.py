# Problem: Maximum Sum Obtained of Any Permutation - https://leetcode.com/problems/maximum-sum-obtained-of-any-permutation/description/

class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        freq = [0] * (len(nums) + 1)

        for start, end in requests:
            freq[start] += 1
            freq[end + 1] -= 1
        
        for i in range(1, len(freq)):
            freq[i] += freq[i - 1]
        
        freq.pop()

        nums.sort(reverse = True)
        freq.sort(reverse = True)

        MOD = 10**9 + 7
        return sum(num * freqs for num, freqs in zip(nums, freq)) % MOD