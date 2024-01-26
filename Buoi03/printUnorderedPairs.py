def printUnorderedPairs(li):
    for i in range(0, len(li)):
        for j in range(i+1, len(li)):
            print(str(li[i]) + "," + str(li[j]))


def printUnorderedPairs(liA, liB):
    for i in range(len(liA)):
        for j in range(len(liB)):
            if liA[i] < liB[j]:
                print(str(liA[i]) + "," + str(liB[j]))


def printUnorderedPairs2(liA, liB):
    for i in range(len(liA)):
        for j in range(len(liB)):
            for k in range(0, 100000):
                print(str(liA[i]) + "," + str(liB[j]))


if __name__ == '__main__':
    myli1 = [1, 2, 3, 4, 5]
    myli2 = [3, 2, 1, 0, 6]

    printUnorderedPairs2(myli1, myli2)
