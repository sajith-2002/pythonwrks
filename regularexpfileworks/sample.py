from re import finditer,findall

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\regularexpfileworks\\sample.txt")

content=f.read()

pattern="https?://[\w\S./]+"

urls=findall(pattern,content)

for url in urls:

    print(url)

