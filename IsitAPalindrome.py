def is_palindrome(s):
    s = list(s.lower())
    if s == s[::-1]:
        return True
    else:
        return False