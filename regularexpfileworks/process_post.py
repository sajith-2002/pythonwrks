from re import fullmatch,finditer

f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\regularexpfileworks\\social_posts.txt")

for line in f:
    post=line.rstrip("\n")

    pattern="#\w+"

    matcher=finditer(pattern,post)

    for obj in matcher:
        print(obj.group())



