def filterDict(myDict, conditionFunc):
    return {k: v for k, v in myDict.items() if conditionFunc(k, v)}


myDict = {'a': 1, 'b': 2, 'c': 3, 'd': 4}

filteredDict = filterDict(myDict, lambda k, v: v % 2 == 0)
print(filteredDict)
