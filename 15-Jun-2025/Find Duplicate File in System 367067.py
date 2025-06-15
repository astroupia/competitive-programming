# Problem: Find Duplicate File in System - https://leetcode.com/problems/find-duplicate-file-in-system/

class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        pth = defaultdict(list)
        for entry in paths:
            parts = entry.split()
            dpth = parts[0]
            
            for file in parts[1:]:
                name, content = file.split('(')
                content = content[:-1] 
                full_path = f"{dpth}/{name}"
                pth[content].append(full_path)
        
        return [group for group in pth.values() if len(group) > 1]