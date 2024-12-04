def last_digit_max(num1,num2):

    num1_lastdigit=num1%10

    num2_lastdigit=num2%10

    print(num1 if num1_lastdigit>num2_lastdigit else num2)

print(last_digit_max(123,456))