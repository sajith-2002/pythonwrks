def swap_dec(fn):

    def wrapper(n1,n2):

        if n1<n2:
            (n1,n2)=(n2,n1)

        return fn(n1,n2)
    



    return wrapper




def round_Dec(fn):

    def wrapper(n1,n2):

        n1=round(n1)
        n2=round(n2)

        return fn(n1,n2)
    
    return wrapper



@swap_dec
@round_Dec
def add_number(num1,num2):

    return num1+num2


@swap_dec
@round_Dec
def substraction(num1,num2):

    return num1-num2


@swap_dec
@round_Dec
def division(num1,num2):

    return num1/num2


print(division(2.7,10.2))
print(add_number(2,10))
print(substraction(2,10))