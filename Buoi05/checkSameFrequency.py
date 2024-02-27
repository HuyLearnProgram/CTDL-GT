def checkSameFrequency(list1, list2):
    if (len(list1) != len(list2)):
        return False
    for i in list1:
        if list1.count(i) != list2.count(i):
            return False

    return True


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 3]

print(checkSameFrequency(list1, list2))
