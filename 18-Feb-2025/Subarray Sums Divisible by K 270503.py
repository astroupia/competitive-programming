# Problem: Subarray Sums Divisible by K - https://leetcode.com/problems/subarray-sums-divisible-by-k/

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        remainder_count = {0: 1}
        running_sum, result = 0, 0

        for num in nums:
            running_sum += num
            remainder = running_sum % k
            if (remainder) in remainder_count:
                result += remainder_count[remainder]
            
            remainder_count[remainder] = remainder_count.get(remainder, 0) + 1
        return result