import re

def longest_palindromic_substring(s):
    pattern = r"^[a-zA-Z0-9]+$"
    if len(s) >= 1 and len(s) <= 1000 and re.match(pattern, s) is not None:
        start_count = 0
        end_count = 0
        while start_count < len(s):
            end_count = start_count + 1
            while end_count < len(s):
                if s[start_count] == s[end_count]:
                    palindrome = True
                    length = end_count - start_count
                    for x in range((length // 2) - 1):
                        if s[start_count + x] != s[end_count - x]:
                            palindrome = False
                    if palindrome:
                        return s[start_count:(end_count + 1)]
                end_count += 1
            start_count += 1
    return ""