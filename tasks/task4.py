def subsequence(s, t):
    i = 0

    for char in t:

        if i < len(s) and s[i] == char:
            i += 1
            
    return i == len(s)


print(subsequence("abc", "ahbgdc"))

print(subsequence("abc", "uvwxyz"))




