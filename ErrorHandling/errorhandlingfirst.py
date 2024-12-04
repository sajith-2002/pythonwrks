num1=int(input("enter num 1 : "))
num2=int(input("enter num 2 : "))

try:

    result=num1/num2
    print(result)

except Exception as e:

    print(e)

print("file write")
print("db commit")