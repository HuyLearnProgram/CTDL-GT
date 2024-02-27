def countWordFrequency(words):
    return {word: words.count(word) for word in words}


words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']

print(countWordFrequency(words))
