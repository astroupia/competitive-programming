# Problem: Books - https://codeforces.com/contest/279/problem/B

n, m = map(int, input().split())
nums = list(map(int, input().split()))

left, sum_time, result = 0, 0, 0

for right in range(len(nums)):
    sum_time += nums[right]

    while sum_time > m:
        sum_time -= nums[left]
        left += 1
    
    result = max(result, right - left + 1)

print(result)
