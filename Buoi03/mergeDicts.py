def mergeDicts(dict1, dict2):
    tempDict = {}
    for key, value in dict1.items():
        if key not in tempDict:
            tempDict[key] = value
        else:
            tempDict[key] += value

    for key, value in dict2.items():
        if key not in tempDict:
            tempDict[key] = value
        else:
            tempDict[key] += value
    return tempDict


if __name__ == '__main__':
    dict1 = {'a': 1, 'b': 2, 'c': 3}
    dict2 = {'b': 3, 'c': 4, 'd': 5}
    print(mergeDicts(dict1, dict2))
