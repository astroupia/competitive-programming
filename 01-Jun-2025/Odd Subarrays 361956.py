# Problem: Odd Subarrays - https://codeforces.com/problemset/problem/1686/B

t = int(input())
for _ in range(t):
    n = int(input())
    p = list(map(int, input().split()))
    ans = 0
    i = 0
    while i < n - 1:
        if p[i] > p[i + 1]:
            ans += 1
            i += 2
        else:
            i += 1
    print(ans)
