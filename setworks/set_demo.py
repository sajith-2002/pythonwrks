st=set()

st={10,20,30}

print(st)

# ________________________________________________________


colors={"red","blue","green"}

colors.add("yellow")

print(colors)

# ________________________________________________________

arr=[10,10,20,30,40,50,40]
st=set()

for num in arr:

    st.add(num)

print(st)

# ________________________________________________________


st1={10,20,30,40,50}

st2={10,20,60,70,80}

intersection_set=st1.intersection(st2)

union_set=st1.union(st2)

difference_set=st1.difference(st2)


print(intersection_set)

print(union_set)

print(difference_set)


# ___________________________________________________________


st1={10,20,30,40,50}

st1.remove(50)

print(st1)

# ___________________________________________

st1={1,2,3}

st2={1,2,3,4,5}

st1.update(st2)

print(st1)

symmetric_diff=st1.symmetric_difference(st2)

print(st1.issubset(st2))

print(st2.issuperset(st1))

print(symmetric_diff)



# __________________________________________________

text="this is a test to remove duplicate words this test is simple"

text2="this simple test remove duplicate words"


words=text.split(" ")


print(set(words))






