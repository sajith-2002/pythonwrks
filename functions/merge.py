text1="ab"

text2="pqrs"

result=""

for i in range(0,len(text1)):

    result+=text1[i]+text2[i]

print(result)






text1="pqrs"

text2="ab"

smallest_text=text1 if text1 < text2 else text2

largest_text=text1 if text1>text2 else text2

result=""
for i in range(0,len(smallest_text)):

    result+=text1[i]+text2[i]

balance_text=largest_text[len(smallest_text):]


result+=balance_text

print(result)




text1="ab"

text2="pqrs"

output=""

for i in range(len(text1)):
    output+=text1[i]

    if i<len(text2):
        output+=text2[i]

print(output)
