from re import finditer

text="i have 3 cars,2 bike and 1 cycle"

pattern="[a-z0-9]"

matcher=finditer(pattern,text)

for m in matcher:

    print(m.start(),"==>",m.group())







# text = "i have 3 cars,2 bikes and 1 cycle"


# for index, char in enumerate(text):
#     if char.isdigit():
#         print(index, char)