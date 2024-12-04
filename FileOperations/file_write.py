

# f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\names.txt","w")

# text="hello world"

# f.write(text)

# f.close()



f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\names.txt","w")

languages=["python","c++","java","php"]

for l in languages:

    f.write(l+"\n")

f.close()