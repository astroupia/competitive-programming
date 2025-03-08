# Problem: Crawler Log Folder - https://leetcode.com/problems/crawler-log-folder/

class Solution:
    def minOperations(self, logs: List[str]) -> int:
        depth = 0  
    
        for operation in logs:
            if operation == "../":
                depth = max(0, depth - 1)
            elif operation == "./":
            
                continue
            else:
        
                depth += 1
            
        return depth