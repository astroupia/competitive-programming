# Problem: Longest k-Good Segment - https://codeforces.com/problemset/problem/616/D

from collections import defaultdict

n, k = map(int, input().split())
nums = list(map(int, input().split()))

count = defaultdict(int)
max_value = [1, 1]

if n <= k:
    print(1, n)
else:
    left = 0
    for right in range(len(nums)):
        count[nums[right]] += 1

        while len(count) > k:
            
            count[nums[left]] -= 1
        
            if count[nums[left]] == 0:
                del count[nums[left]]
            
            left += 1
        
        if right - left  > max_value[1] - max_value[0]:
            max_value = [left + 1, right + 1]
    
    if not max_value:
        print(1, n)
    else:
        print(*max_value)
