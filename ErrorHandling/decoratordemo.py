def swap_dec(fn):

    def wrapper(n1,n2):

        if n1<n2:

            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    return wrapper



@swap_dec
def sub(num1,num2):


    return num1-num2

@swap_dec
def div(num1,num2):


    return num1/num2

print(sub(10,20))
print(div(10,2))