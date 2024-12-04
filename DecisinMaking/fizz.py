num = int(input("Enter the number:"))

if num % 15 == 0:

    print('fizzbuzz')

elif num % 3 == 0:

    print('fizzz')

elif num % 5 == 0:

    print('buzzz')

else:
    
    print('invalid num')
