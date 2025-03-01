# Problem: D - Bernabas and the Harmonious Melody - https://codeforces.com/gym/588468/problem/D

import sys

def min_removals_to_palindrome(n, s):
    def is_palindrome_with_removal(s, char_to_remove):
        left, right = 0, len(s) - 1
        removals = 0
        
        while left < right:
            if s[left] == s[right]:
                left += 1
                right -= 1
            elif s[left] == char_to_remove:
                left += 1
                removals += 1
            elif s[right] == char_to_remove:
                right -= 1
                removals += 1
            else:
                return float('inf')  
        
        return removals

    if s == s[::-1]:
        return 0

    min_deletions = float('inf')
    for char in set(s):  
        min_deletions = min(min_deletions, is_palindrome_with_removal(s, char))

    return min_deletions if min_deletions != float('inf') else -1

if __name__ == "__main__":
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    t = int(data[index])
    index += 1
    results = []
    
    for _ in range(t):
        n = int(data[index])
        index += 1
        s = data[index]
        index += 1
        results.append(str(min_removals_to_palindrome(n, s)))
    
    sys.stdout.write("\n".join(results) + "\n")
