#remove duplicates

arr=[1,2,3,4,5,4,5,6,3]

duplicates=[]

arr.sort()

for element in arr:

    if element not in duplicates:

        duplicates.append(element)

print('duplicates removed : ',duplicates)