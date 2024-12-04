words=["hai","hello","this","hai","is","hello","this","that"]

word_frequency={w:words.count(w) for w in words}

print(word_frequency) #{'hai': 2, 'hello': 2, 'this': 2, 'is': 1}

recursive_words=[k for k,v in word_frequency.items() if v>1]

print(recursive_words)



# display non_recursive words


non_recursive_words=[k for k,v in word_frequency.items() if v==1 ]        

print(non_recursive_words)