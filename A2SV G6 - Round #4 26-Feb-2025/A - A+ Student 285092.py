# Problem: A - A+ Student - https://codeforces.com/gym/590053/problem/A

t = int(input())

for _ in range(t):
    nums = list(map(int, input().split()))
    
    student_a = max(0, max(nums[1], nums[2]) + 1 - nums[0])
    student_b = max(0, max(nums[0],  nums[2]) + 1 - nums[1])
    student_c = max(0, max(nums[0], nums[1]) + 1 - nums[2])

    print(student_a, student_b, student_c)