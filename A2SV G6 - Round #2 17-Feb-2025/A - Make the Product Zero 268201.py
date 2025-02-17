# Problem: A - Make the Product Zero - https://codeforces.com/gym/586960/problem/A

from math import inf

length = int(input())
nums = list(map(int, input().split()))

if 0 in nums:
    print(0)
else:
    min_num  = float(inf)
    for num in nums:
        min_num = min(min_num, abs(num))
    print(min_num)