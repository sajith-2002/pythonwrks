text=input('enter the text :')

length=len(text)-1

reversed_str=""

for i in range(length,-1,-1):

    reversed_str+=text[i]

print(reversed_str)






text='helloworld'

print(text.index('o'))