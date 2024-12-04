f=open("C:\\Users\\HP\\Desktop\\Pythonworks\\datasets\\qustion.txt")

words=[]

for line in f:

    line=line.rstrip("\n")

    all_words=line.split(" ")

    for w in all_words:

        words.append(w)

word_count={w:words.count(w) for w in words}

nested_list=[[v,k] for k,v in word_count.items()]


print(sorted(nested_list,reverse=True))