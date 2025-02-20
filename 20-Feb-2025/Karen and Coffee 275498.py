# Problem: Karen and Coffee - https://codeforces.com/contest/816/problem/B

import sys

def main():
    input = sys.stdin.readline
    n, k, q = map(int, input().split())
    MAX_TEMP = 200001  
    
    diff = [0] * (MAX_TEMP + 1)
    for _ in range(n):
        l, r = map(int, input().split())
        diff[l] += 1
        diff[r+1] -= 1

  
    freq = [0] * (MAX_TEMP)
    freq[1] = diff[1]
    for i in range(2, MAX_TEMP):
        freq[i] = freq[i-1] + diff[i]
    
    
    admissible = [0] * (MAX_TEMP)
    for i in range(1, MAX_TEMP):
        if freq[i] >= k:
            admissible[i] = 1

    
    prefix = [0] * (MAX_TEMP)
    prefix[1] = admissible[1]
    for i in range(2, MAX_TEMP):
        prefix[i] = prefix[i-1] + admissible[i]

    
    out = []
    for _ in range(q):
        a, b = map(int, input().split())
        res = prefix[b] - (prefix[a-1] if a > 1 else 0)
        out.append(str(res))
    
    sys.stdout.write("\n".join(out))

if __name__ == "__main__":
    main()
