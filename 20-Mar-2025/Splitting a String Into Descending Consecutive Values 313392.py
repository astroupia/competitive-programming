# Problem: Splitting a String Into Descending Consecutive Values - https://leetcode.com/problems/splitting-a-string-into-descending-consecutive-values/

class Solution:
    def splitString(self, s: str) -> bool:
        def split(path, i):
            if i == len(s):
                if len(path) < 2:
                    return False
                for j in range(1, len(path)):
                    if path[j-1] - 1 != path[j]:
                        return False
                return True
            if len(path) > 1 and path[-2] - 1 != path[-1]:
                return False
            num = 0
            for j in range(i, len(s)):
                num = 10 * num + int(s[j])
                path.append(num)
                if split(path, j + 1):
                    return True
                path.pop()
            return False
        return split([], 0)