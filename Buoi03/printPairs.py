def printPairs(li):
    for i in li:
        for j in li:
            print(str(i)+","+str(j))


if __name__ == '__main__':
    myList = [1, 2, 3, 4, 5]
    printPairs(myList)
