# Problem: Boats to Save People - https://leetcode.com/problems/boats-to-save-people/

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        left, right, boats = 0, len(people) - 1, 0
        people.sort()
        while left <= right:
            if people[left] + people[right] <= limit:
                boats += 1
                left += 1
                right -= 1
            else:
                boats += 1
                right -= 1
        
        return boats
