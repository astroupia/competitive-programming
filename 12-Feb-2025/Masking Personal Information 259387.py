# Problem: Masking Personal Information - https://leetcode.com/problems/masking-personal-information/description/?envType=problem-list-v2&envId=string

import re

class Solution:
    def maskPII(self, s: str) -> str:
        if "@" in s: 
            name, domain = s.lower().split("@")
            masked_name = name[0] + "*****" + name[-1]
            return masked_name + "@" + domain
        else:
            nums = re.sub(r"\D", "", s) 
            local_number = "***-***-" + nums[-4:]  
            country_code_length = len(nums) - 10

            if country_code_length == 0:
                return local_number
            else:
                return "+" + "*" * country_code_length + "-" + local_number
