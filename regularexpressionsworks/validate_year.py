from re import fullmatch

pattern="((18|19)[0-9]{2}|200[0-9]|201[0-9]|202[0-4])"

year=input("enter year :")

matcher=fullmatch(pattern,year)

print("invalid" if matcher == None else "valid")
