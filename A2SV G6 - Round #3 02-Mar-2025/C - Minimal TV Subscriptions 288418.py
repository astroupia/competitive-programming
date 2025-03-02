# Problem: C - Minimal TV Subscriptions - https://codeforces.com/gym/588468/problem/C

t = int(input())
for _ in range(t):
    n, k, d = map(int, input().split())
    a = list(map(int, input().split()))
    freq = {}
    for i in range(d):
        freq[a[i]] = freq.get(a[i], 0) + 1
    min_subscriptions = len(freq)
    for i in range(d, n):
        left = a[i - d]
        freq[left] -= 1
        if freq[left] == 0:
            del freq[left]
        right = a[i]
        freq[right] = freq.get(right, 0) + 1
        unique_shows = len(freq)
        min_subscriptions = min(min_subscriptions, unique_shows)
    print(min_subscriptions)