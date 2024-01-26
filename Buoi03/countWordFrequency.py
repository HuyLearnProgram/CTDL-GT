def countWordFrequency(words):
    countWords = {}
    for value in words:
        if value not in countWords:
            countWords[value] = 1
        else:
            countWords[value] += 1
    return countWords


if __name__ == '__main__':
    words = ['apple', 'orange', 'banana', 'apple', 'orange', 'apple']
    print(countWordFrequency(words))
