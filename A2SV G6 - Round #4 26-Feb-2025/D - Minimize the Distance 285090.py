# Problem: D - Minimize the Distance - https://codeforces.com/gym/590053/problem/D

num = int(input())

nums = list(map(int, input().split()))
nums.sort()
print(nums[(num - 1) // 2])
