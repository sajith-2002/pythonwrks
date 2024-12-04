from re import finditer

text="fatcatrunsveryfasttocatchtherat"

matcher=finditer("at",text)

for m in matcher:

    print(m.start(),m.group())