# Problem: E - Symmetrization - https://codeforces.com/gym/586960/problem/E

def solve():
    n = int(input())
    arr = []
    for i in range(n):
        arr.append(list(map(int, input())))
    
    if n == 1:
        print(0)
        return
 
    t, b = 0, n - 1
    l, r = 0, n - 1
 
    ans = 0    
    tmp = [[], [], [], []]
    while t < b and l < r:
        for i in range(l, r + 1):
            tmp[0].append(arr[t][i])
        for i in range(t, b + 1):
            tmp[1].append(arr[i][r])
        for i in range(r, l - 1, -1):
            tmp[2].append(arr[b][i])
        for i in range(b, t - 1, -1):
            tmp[3].append(arr[i][l])
        for i in range(len(tmp[-1]) - 1): 
            cur = 0
            for j in range(4):
                if tmp[j][i] == 1:
                    cur += 1
            if cur > 2:
                ans += 4 - cur
            else:
                ans += cur
            
        tmp = [[], [], [], []]
 
        t, b = t + 1, b - 1
        l, r = l + 1, r - 1
    print(ans)
 
if __name__ == "__main__":
    t = 1
    t = int(input().strip())
    for _ in range(t):
        solve()
