user_ip=input("enter bracket pairs: ")


symboldic={

    "{":"}",
    "(":")",
    "[":"]",
    "<":">"
}


symbolstack=[]


top=-1

is_valid=True

for symbol in user_ip:

    if symbol in symboldic:

        top=top+1

        symbolstack.append(symbol)

    elif top==-1:

        is_valid=False


    elif symbol ==symboldic.get(symbolstack[top]):

        top=top-1

        symbolstack.pop()

    else:

        is_valid=False

if len(symbolstack)==0 and is_valid==True:

    print("valid")

else:

    print("invalid")









    