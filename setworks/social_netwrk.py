users=["rahul","rohit","kohli","rishab","sanju","pandya","siraj"]

rahul_followers=["rohit","kohli","rishab"]

sanju_followers=["sanju","rohit","kohli"]

rahul_follow_suggestion=set(users).difference(set(rahul_followers))

mutual_freinds=set(rahul_followers).intersection(set(sanju_followers))

print(rahul_follow_suggestion)



