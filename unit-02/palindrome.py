def is_palindrome(s: str):
    def to_chars(s: str) -> str:
        s = s.lower()
        ans = ""
        for c in s:
            if c in "abcdefghijklmnopqrstuvwxyz":
                ans = c + ans
        return ans

    def _is_pal(s: str) -> bool:
        if len(s) == 0 or len(s) == 1:
            return True
        return s[0] == s[-1] and _is_pal(s[1:-1])

    return _is_pal(to_chars(s))

if __name__ == "__main__":
    print(is_palindrome("abba"))
