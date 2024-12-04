num1 = int(input('Enter number 1: '))
num2 = int(input('Enter number 2: '))
num3 = int(input('Enter number 3: '))


if (num1 > num2 and num1 < num3) or (num1 > num3 and num1 < num2):
    second_largest = num1

elif (num2 > num1 and num2 < num3) or (num2 > num3 and num2 < num1):
    second_largest = num2
    
else:
    second_largest = num3

print(f'The second largest number is: {second_largest}')
