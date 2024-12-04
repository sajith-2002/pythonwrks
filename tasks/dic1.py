

# 1. Create a dictionary to store the names and ages of 5 people. Access and print the age of one person using their name.



# names={"sanku":23,"josh":22,"hansu":23,"sanju":23,"sreeku":22}

# print(names.get("sanku"))



# 2. Write a Python program to merge two dictionaries.

# names1={"sanku":23,"josh":22,"hansu":23,"sanju":23,"sreeku":22}

# names2={"sanku2":23,"josh2":22,"hansu2":23,"sanju2":23,"sreeku2":22}

# names1.update(names2)

# print(names1)








# 3. Given a dictionary where the keys are student names and the values are their scores, write a program to calculate the average score.

# student_scores={"sanku":23,"josh":22,"hansu":23,"sanju":23,"sreeku":22}

# total= sum(student_scores.values())

# numberofstudents=len(student_scores)

# avg= total/numberofstudents

# print(avg)







# 4. Write a dictionary comprehension to create a dictionary where the keys are numbers from 1 to 10 and the values are the squares of those numbers.

# squares = {num: num**2 for num in range(1, 11)}

# print(squares)





# 5. Write a Python program to create a dictionary from a list of keys and values using dictionary comprehension.

# keys = ['name', 'age', 'city', 'job']

# values = ['josh', 30, 'ekm', 'Engineer']


# dictionary = {keys[i]: values[i] for i in range(len(keys))}

# print(dictionary)






# 6. Given two lists, one with fruits and the other with prices, write a dictionary comprehension to pair them together into a dictionary.


# fruits = ['apple', 'banana', 'mango', 'orange']

# prices = [100, 40, 75, 150]

# fruit_price_dict = {fruits[i]: prices[i] for i in range(len(fruits))}

# print(fruit_price_dict)




# 7. Write a Python program to filter a dictionary, keeping only items with values greater than 50 using dictionary comprehension.

# items ={'apple':10, 'banana':120, 'mango':30, 'orange':90}

# filtered_dict = {key: value for key, value in items.items() if value > 50}

# print(filtered_dict)






# 8. Given a sentence, count the frequency of each word using a dictionary.


# sentence = "this is a test this is only a test"


# words = sentence.split()


# word_count = {word: words.count(word) for word in words}

# print(word_count)





# 9. Write a dictionary comprehension to convert all the values in a dictionary to their absolute values.


# num = [1,23,-56,99,46,-43]

# abs_dict = {num:abs(num) for num in num}

# print(abs_dict)




# 10. Given a dictionary of items and their prices, write a program to apply a 10% discount to all the items using dictionary comprehension.

items = {'apple': 100,'banana': 40,'cherry': 75,'date': 150}


discounted_items = {item: price * 0.9 for item, price in items.items()}

print(discounted_items)




