def most_frequent_word(text):

    text=text.lower()

    words=text.split(" ")

    word_dictionary={}

    for w in words:

        if w in word_dictionary:

            word_dictionary[w]+=1

        else:

            word_dictionary[w]=1

    print(word_dictionary)

    most_frequent=max(word_dictionary,key=word_dictionary.get)

    return most_frequent

text = "Hello world! Hello everyone. Welcome to the world."

print("Most frequent word is :",most_frequent_word(text))