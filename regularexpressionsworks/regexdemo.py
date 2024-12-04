from re import finditer

text="ababababab"

matcher=finditer("ab",text)

for m in matcher:

    print(m.start(),m.group())