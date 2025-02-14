# Problem: Alternating Subsequence - https://codeforces.com/contest/1343/problem/C

t = int(input())

for _ in range(t):
    num = int(input())
    nums = list(map(int, input().split()))
    
    result = [nums[0]]

    for ptr in range(1, len(nums)):
        if nums[ptr] < 0:
            if result[-1] <= nums[ptr] and result[-1] < 0:
                result[-1] = nums[ptr]
            elif result[-1] > 0: 
                result.append(nums[ptr])
        else:
            if result[-1] > 0 and nums[ptr] >= result[-1]:
                result[-1] = nums[ptr]
            elif result[-1] < 0:
                result.append(nums[ptr])
                
    print(sum(result))