num1=int(input("enter num 1 : "))
num2=int(input("enter num 2 : "))


try:

    result=num1/num2

    print(result)

except:

    num2=int(input("enter num which is divisible by num1 : "))

    result=num1/num2

    print(result)

finally:

 print("file")
 print("db commit")

