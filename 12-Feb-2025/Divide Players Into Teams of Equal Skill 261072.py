# Problem: Divide Players Into Teams of Equal Skill - https://leetcode.com/problems/divide-players-into-teams-of-equal-skill/

class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        sum_chemistry, left, right = 0, 0, len(skill) - 1
        skill.sort()
        summation = skill[left] + skill[right]

        while left < right:
            if skill[left] + skill[right] != summation:
                return -1

            sum_chemistry += (skill[left] * skill[right])
            left += 1
            right -= 1
            
        return sum_chemistry
