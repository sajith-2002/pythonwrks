arr=[2,3,4,5,6]

map_num=[num+1 if num>5 else num-1 for num in arr]












cubes=[]

for num in arr:

    cubes.append(num**3)

print(cubes)



cubes=[num**3 for num in arr]

print(cubes)



add_ten=[num+10 for num in arr]
print(add_ten)


odd_numbers=[num for num in arr if num%2!=0]
print(odd_numbers)


even_numbers=[num for num in arr if num%2==0]
print(even_numbers)

num_gt_five=[num for num in arr if num > 5]
print(num_gt_five)