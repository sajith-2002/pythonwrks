expenses = [10000, 11000, 12000, 13000]


min_expense = expenses[0]


for exp in expenses:
    if exp < min_expense:
        min_expense = exp

print("Minimum expense:", min_expense)
