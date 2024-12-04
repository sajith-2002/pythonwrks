from re import finditer

text="ababababab"

matcher=finditer("ba",text)

for m in matcher:

    print(m.start(),m.group())