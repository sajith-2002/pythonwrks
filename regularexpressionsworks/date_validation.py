from re import fullmatch

pattern="(0?[1-9|[12][0-9]|3[01])"

date=input("enter date :")

matcher=fullmatch(pattern,date)

print("invalid" if matcher == None else "valid")
