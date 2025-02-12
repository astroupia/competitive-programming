# Problem: Pass the Pillow - https://leetcode.com/problems/pass-the-pillow/description/

class Solution:
    def passThePillow(self, n: int, time: int) -> int:
        lst = [i + 1 for i in range(n)]

        if time < n:
            return time + 1
        
        round_count = time // (n - 1) 
        hold_value = time % (n - 1)

        if round_count % 2 == 0:
            return lst[hold_value]
        else:
            return lst[-1-hold_value]

            