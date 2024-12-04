text='vipinkumar@gmail.com'


print(text[0:text.index("@")])
    
 



text="hellopython"

o_index=text.index("o")

rev_sub_string=text[o_index-1::-1]

bal_sub_string=text[o_index:]

result=rev_sub_string+bal_sub_string

print(result)