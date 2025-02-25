# Problem: Partition Labels - https://leetcode.com/problems/partition-labels/

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        count = defaultdict(int)

        for i in range(len(s)):
            count[s[i]] = i
        
        left, right, start = 0, 0, 0
        result = []

        while left < len(s):
           
            right = max(right, count[s[left]])

            if left == right:
                result.append(right - start + 1)
                start = left + 1
            
            left += 1

        return result 

                
            



