# Problem: F - Array Transformation - https://codeforces.com/gym/586960/problem/F

from collections import Counter

def min_operations(arr):
    n = len(arr)
    freq = Counter(arr)
    max_count = max(freq.values())
    count_map = {i: 0 for i in range(1, max_count + 1)}

    for value in freq.values():
        for i in range(1, value + 1):
            count_map[i] += 1

    result = float('inf')
    for key, value in count_map.items():
        result = min(result, n - value * key)

    return result

t = int(input())

for _ in range(t):
    _ = int(input())
    arr = list(map(int, input().split()))
    print(min_operations(arr))
