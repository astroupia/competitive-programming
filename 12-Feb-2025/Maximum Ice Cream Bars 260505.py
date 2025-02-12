# Problem: Maximum Ice Cream Bars - https://leetcode.com/problems/maximum-ice-cream-bars/

class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        sum_price = [0] * len(costs)
        sum_price[0] = costs[0]
        count = 0 

        for i in range(1, len(sum_price)):
            sum_price[i] = sum_price[i-1] + costs[i]

        for i in range(len(sum_price)):
            if sum_price[i] <= coins:
                count += 1

        return count 
