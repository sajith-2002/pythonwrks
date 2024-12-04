arr=[10,20,30,40,2,3]

#result={key:value iteration condition}

result={num:num**3 for num in arr}

print(result)


even_squares={num:num**2 for num in arr if num %2==0}

print(even_squares)

odd_sums={num: num**3 for num in arr if num%2!=0}

print(odd_sums)


frequency_count={num:arr.count(num)for num in arr}

print(frequency_count)