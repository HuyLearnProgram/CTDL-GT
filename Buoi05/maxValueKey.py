def maxValueKey(myDict):
    valMax = 0
    keyMax = ''
    for key, value in myDict.items():
        if value > valMax:
            valMax = value
            keyMax = key
    return keyMax


myDict = {'a': 5, 'b': 9, 'c': 2}

print(maxValueKey(myDict))
