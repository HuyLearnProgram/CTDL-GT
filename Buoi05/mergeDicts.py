def mergeDicts(dict1, dict2):
    tempDict = dict.copy(dict1)
    for i in dict2:
        if i not in tempDict:
            tempDict[i] = dict2[i]
        else:
            tempDict[i] += dict2[i]
    return tempDict


dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'b': 3, 'c': 4, 'd': 5}

print(mergeDicts(dict1, dict2))
