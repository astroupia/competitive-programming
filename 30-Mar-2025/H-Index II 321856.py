# Problem: H-Index II - https://leetcode.com/problems/h-index-ii/description/

class Solution:
    def hIndex(self, citations: List[int]) -> int:
    
        n = len(citations)
        low, high, h_index = 0, n - 1, 0
        while low <= high:
            mid = (low + high) // 2
            if citations[mid] >= n - mid:
                h_index = n - mid
                high = mid - 1
            else:
                low = mid + 1
        return h_index
