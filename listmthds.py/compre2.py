text=["apple","iphone","orenge","potatto","tomatto"]


vowels = ['a', 'e', 'i', 'o', 'u']

words_starting_with_vowels = [word for word in text if word[0] in vowels]

print(words_starting_with_vowels)

consonent_words = [word for word in text if word[0] not in vowels]

print(consonent_words)


long = max([len(word) for word in text])

longest_word = [word for word in text if len(word)==long ]

print(longest_word)

