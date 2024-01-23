def countWordFrequency(words):
    countWords = {}
    for key, value in enumerate(words):
        if value not in countWords:
            countWords[value] = 1
        else:
            countWords[value] += 1
    return countWords


if __name__ == '__main__':
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
    print(countWordFrequency(words))
