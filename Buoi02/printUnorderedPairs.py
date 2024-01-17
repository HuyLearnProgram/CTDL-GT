import array


def printUnorderedPairs(array):
    for i in range(0, len(array)):
        for j in range(i+1, len(array)):
            print(str(array[i]) + "," + str(array[j]))


def printUnorderedPairs(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            if arrayA[i] < arrayB[j]:
                print(str(arrayA[i]) + "," + str(arrayB[j]))


def printUnorderedPairs2(arrayA, arrayB):
    for i in range(len(arrayA)):
        for j in range(len(arrayB)):
            for k in range(0, 100000):
                print(str(arrayA[i]) + "," + str(arrayB[j]))


if __name__ == '__main__':
    myArray1 = array.array('i', [1, 2, 3, 4, 5])
    myArray2 = array.array('i', [3, 2, 1, 0, 6])

    printUnorderedPairs2(myArray1, myArray2)
