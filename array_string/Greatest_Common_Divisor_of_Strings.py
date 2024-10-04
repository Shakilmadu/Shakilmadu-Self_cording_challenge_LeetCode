
## // https://leetcode.com/greatest-common-divisor-of-strings/description/

import math
def gcd_of_strings(str1: str, str2: str) -> str:
    # Helper function to check if one string can be constructed by repeating another string
    def is_divisible(s: str, t: str) -> bool:
        return s == t * (len(s) // len(t))


    gcd_len = math.gcd(len(str1), len(str2))

    # Candidate for gcd string
    candidate = str1[:gcd_len]

    # Check if the candidate divides
    if is_divisible(str1, candidate) and is_divisible(str2, candidate):
        return candidate
    else:
        return ""

str1 = "ABCABC"
str2 = "ABC"
result = gcd_of_strings(str1, str2)
print(result)
