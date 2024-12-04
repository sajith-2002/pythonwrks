from re import fullmatch,finditer,findall

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\regularexpfileworks\\data.txt")

content=f.read()

pattern="[0-9]{2}/[0-9]{2}/[0-9]{4}"

dates=findall(pattern,content)

for date in dates:

    print(date)
