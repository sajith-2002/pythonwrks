#2nd largest elements

arr=[5,8,3,1,5,9,8,4]

largest=max(arr)

while largest in arr:

    arr.remove(largest)

second_largest=max(arr)

print('second largest = ',second_largest)