s = "Malayalam"

def is_palindrome(s):
    # s == s[::-1] one line code
    short_s = s.lower()

    left = 0
    right = len(short_s) - 1

    while left < right:

        if short_s[left] != short_s[right]:
            return False

        left += 1
        right -= 1

    return True

print(is_palindrome(s))