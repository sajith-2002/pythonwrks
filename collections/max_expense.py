expenses = [10000, 11000, 12000, 13000]


max_expense = expenses[0]

for exp in expenses:
    if exp > max_expense:
        max_expense = exp

print("Maximum expense:", max_expense)
