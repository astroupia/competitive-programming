# Problem: Lemonade Change
easy - https://leetcode.com/problems/lemonade-change/

class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        bill_count = defaultdict(int)

        for i in range(len(bills)):
            bill_count[bills[i]] += 1
        
            if bills[i] == 10:
                if bill_count[5] > 0:
                    bill_count[5] -= 1
                else:
                    return False
            elif bills[i] == 20:
                if bill_count[10] > 0 and bill_count[5] > 0:
                    bill_count[10] -= 1
                    bill_count[5] -= 1
                elif bill_count[5] > 2:
                    bill_count[5] -= 3
                else:
                    return False
                
        return True