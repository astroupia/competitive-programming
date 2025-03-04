# Problem: Rabbits in Forest - https://leetcode.com/problems/rabbits-in-forest/

class Solution:
    def numRabbits(self, answers: List[int]) -> int:
        count = defaultdict(int)
        freq =  Counter(answers)

        min_rabbits = 0 

        for ans in answers:
            if count[ans] == 0:
                min_rabbits += ans + 1
                count[ans] = ans
            else:
                count[ans] -= 1

        return min_rabbits