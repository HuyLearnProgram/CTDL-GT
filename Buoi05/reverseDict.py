def reverseDict(myDict):
    tempDict = dict()
    for key, value in myDict.items():
        tempDict[value] = key
    return tempDict


myDict = {'a': 1, 'b': 2, 'c': 3}
print(reverseDict(myDict))
