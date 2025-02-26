# Problem: B - Jo's Adventure - https://codeforces.com/gym/590053/problem/B

n, m = map(int, input().split())
nums = list(map(int, input().split()))

prefix = [0] * n
sufix = [0] * n

for i in range(1, n):
    prefix[i] = prefix[i - 1] + max(0, nums[i - 1] - nums[i])

for i in range(1, n):
    sufix[i] = sufix[i - 1] + max(0, nums[i] - nums[i - 1])

for _ in range(m):
    p, q = map(int, input().split())

    p -= 1
    q -= 1
    
    if p < q:
        print(prefix[q] - prefix[p])
    else:
        print(sufix[p] - sufix[q])
