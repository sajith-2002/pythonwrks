text="hello,wrld,python"

words=text.split("   ")

print(words)



text="\t this is \ta line\t"

new_text=text.strip("\t")

print(new_text)




text="hello world program"

new_text=text.replace("o","a")

print(new_text)




text="python programming"

print(text[7:])

print(text[::2])


string="hello"

reversed_text=string[::-1]

print(reversed_text)
