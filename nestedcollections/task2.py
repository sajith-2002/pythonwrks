source="chicken"

target="hens"

# char_count={}

# for ch in source:

#     if ch in char_count:

#         char_count[ch]+=1

#     else:

#         char_count[ch]=1

# print(char_count)

char_count={ch:source.count(ch) for ch in source}

is_kangaro_wrd=True

for ch in target:

    if ch in char_count and char_count.get(ch)>0:

        char_count[ch]-=1

    else:
        
        is_kangaro_wrd=False

        break

print(is_kangaro_wrd)
