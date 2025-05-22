# Problem: Bitwise XOR of All Pairings - https://leetcode.com/problems/bitwise-xor-of-all-pairings/description/?envType=problem-list-v2&envId=brainteaser

class Solution:
    def xorAllNums(self, nums1: List[int], nums2: List[int]) -> int:
        xor1 = 0
        for num in nums1:
            xor1 ^= num
        xor2 = 0
        for num in nums2:
            xor2 ^= num
        res, m, n = 0, len(nums1), len(nums2)
        if n % 2 == 1:
            res ^= xor1
        if m % 2 == 1:
            res ^= xor2
        return res