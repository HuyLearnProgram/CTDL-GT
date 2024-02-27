def checkPalindrome(s):
    s = s.lower()
    # Initialize two pointers, one at the beginning and one at the end
    start, end = 0, len(s) - 1

    while start < end:
        # Skip non-alphanumeric characters from the left
        while start < end and not s[start].isalnum():
            start += 1

        # Skip non-alphanumeric characters from the right
        while start < end and not s[end].isalnum():
            end -= 1

        # Compare characters
        if s[start] != s[end]:
            return False

        # Move pointers towards each other
        start += 1
        end -= 1

    return True


inp = "A man, a plan, a canal, Panama"
inp2 = "level"
inp = inp.lower()
print(inp)
print(checkPalindrome(inp))
