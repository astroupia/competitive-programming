# Problem: Fair Distribution of Cookies - https://leetcode.com/problems/fair-distribution-of-cookies/

class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse=True)  
        children = [0] * k        
        fairness = float("inf")   

        def fair(i):
            nonlocal fairness
            if i == len(cookies):  
                fairness = min(fairness, max(children))
                return
            if max(children) >= fairness:  
                return
            for j in range(k):  
                children[j] += cookies[i]
                fair(i + 1)
                children[j] -= cookies[i] 

        fair(0)
        return fairness