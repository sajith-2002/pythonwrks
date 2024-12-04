orders=["tea","coffee","tea","cofee","gheeroast","plainroast","porotta","tea"]

summary_dic={}

for item in orders:

    if item in summary_dic:

        summary_dic[item]+=1

    else:

        summary_dic[item]=1

print(summary_dic)