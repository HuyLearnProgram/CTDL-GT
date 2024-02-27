def checkAnagram(s1, s2):
    s1 = s1.lower()
    s2 = s2.lower()
    # Remove non-alphanumeric characters
    s1 = ''.join(c for c in s1 if c.isalnum())
    s2 = ''.join(c for c in s2 if c.isalnum())

    # Check if the sorted characters of both words are the same
    return sorted(s1) == sorted(s2)


print(checkAnagram("restful", "fluster"))
