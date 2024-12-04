def number_to_words(number):
    if number < 0 or number >= 900:
        return "Number out of range"

    units = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    teens = ["ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
    tens = ["", "", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]

    words = ""
    if number >= 100:
        words += units[number // 100] + " hundred"
        number %= 100
        if number > 0:
            words += " "

    if 10 <= number < 20:
        words += teens[number - 10]
    else:
        words += tens[number // 10]
        if number % 10 > 0 and number >= 20:
            words += " "
        words += units[number % 10]

    return words.strip()

# Get input from user
num = int(input("Enter a number less than 900: "))
print(number_to_words(num))
