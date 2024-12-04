f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\fruits.txt")

fruits=[]

for line in f:

    fruits.append(line.rstrip("\n"))

print(fruits)