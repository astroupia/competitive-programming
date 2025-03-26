# Problem: The Meeting Place Cannot Be Changed - https://codeforces.com/problemset/problem/780/B

num = int(input())
friends = list(map(int, input().split()))
times = list(map(int, input().split()))
eps = 10 ** -6

def check(value):
    _max = float("-inf")
    for i in range(len(friends)):
        diff = abs(friends[i] - value) 
        time = diff / times[i]
        _max = max(_max, time)
    
    return _max

left = min(friends)
right = max(friends)

while right - left > eps:
    mid = (left + right) / 2
    if check(mid) > check(mid + eps):
        left = mid
    else:
        right = mid
    
print(f"{check(left):.6f}")