# Problem: F - Binary Substrings with Exactly k Ones - https://codeforces.com/gym/588468/problem/F

from collections import defaultdict

seen = defaultdict(int)
seen[0] = 1
k = int(input())
binary = input()

res = 0
running_sum = 0

for i, num in enumerate(binary):
    running_sum += int(num)

    if running_sum - k in seen:
        res += seen[running_sum - k]
    
    seen[running_sum] += 1

print(res)