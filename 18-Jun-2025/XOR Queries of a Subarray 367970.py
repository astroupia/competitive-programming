# Problem: XOR Queries of a Subarray - https://leetcode.com/problems/xor-queries-of-a-subarray/

class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [0] * (len(arr) + 1)
    
        for i in range(len(arr)):
            prefix[i + 1] = prefix[i] ^ arr[i]
        
        result = []
        for left, right in queries:
            result.append(prefix[right + 1] ^ prefix[left])
        
        return result