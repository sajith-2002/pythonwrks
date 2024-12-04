#lambda functions

add=lambda num1,num2:num1+num2

print(add(100,200))


cube=lambda num:num**3

print(cube(4))


sub=lambda num1,num2:num1-num2

print(sub(10,5))


max_two=lambda str1,str2:str1 if len(str1) > len(str2) else str2

print(max_two("apple","mangos"))



min_two=lambda str1,str2:str1 if len(str1) < len(str2) else str2

print(min_two("apple","mangos"))


smart_sub=lambda num1,num2:num1-num2 if num1>num2 else num2-num1

print(smart_sub(20,100))




words=["hello","hai","morning","test","apple"]

def get_length(word):

    return len(word)

print(max(words,key=get_length)) 