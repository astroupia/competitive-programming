# Problem: C - Binary Flip - https://codeforces.com/gym/590053/problem/C

t = int(input())

for _ in range(t):
    num = int(input())
    first_nums = list(map(int, input().strip()))
    second_nums = list(map(int, input().strip()))
    left = - 1 
    diff = count = 0
    flag = True

    for r in range(len(first_nums)):
        if  first_nums[r] != second_nums[r]:
            diff += 1
        
        if first_nums[r] == 1:
            count += 1
        
        if count * 2 == r + 1:
            if diff != 0 and diff != r - left:
                flag = False
                break
            diff = 0
            left = r
 
    if diff != 0 and diff != num - left:
        flag = False

    if flag:
        print("YES")
    else:
        print("NO")
    