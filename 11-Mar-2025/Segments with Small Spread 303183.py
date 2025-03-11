# Problem: Segments with Small Spread - https://codeforces.com/edu/course/2/lesson/9/2/practice/contest/307093/problem/F

from collections import deque

def count_good_segments(n, k, a):
    if n == 0:
        return 0
    
    max_deque = deque()
    min_deque = deque()
    total = 0
    left = 0
    
    for right in range(n):
        while max_deque and a[max_deque[-1]] <= a[right]:
            max_deque.pop()
        max_deque.append(right)
        
        while min_deque and a[min_deque[-1]] >= a[right]:
            min_deque.pop()
        min_deque.append(right)
        
        while max_deque and min_deque and a[max_deque[0]] - a[min_deque[0]] > k:
            if max_deque[0] == left:
                max_deque.popleft()
            if min_deque[0] == left:
                min_deque.popleft()
            left += 1
        
        total += right - left + 1
    
    return total

n, k = map(int, input().split())
a = list(map(int, input().split()))
result = count_good_segments(n, k, a)
print(result)
